import logging
import random
from collections import defaultdict, namedtuple
from itertools import product
from pathlib import Path
from time import time

import numpy
import pandas as pd
from deap import base, creator, tools

from schedulebot.genetic import elitism, graphs
from schedulebot.utils.date_generation import get_date_string
from schedulebot.utils.fs import load_graph, read_json, read_yaml
from schedulebot.utils.load import get_days, get_groups, get_time_intervals
from schedulebot.utils.viz import plot_fitness

CURRENT_DPATH = Path(__file__).parent.resolve()
PROJECT_DPATH = CURRENT_DPATH.parent
DATA_DPATH = PROJECT_DPATH / "data"
CONFIG_DPATH = PROJECT_DPATH / "configs"
GRAPH_DPATH = DATA_DPATH / "graph"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__file__)

ScheduleSolution = namedtuple("ScheduleSolution", field_names=["gcp", "best_individual", "logbook"])


def generate_schedule(graph, config: dict) -> ScheduleSolution:
    toolbox = base.Toolbox()

    max_colors = config["max_colors"] - 1

    # create the graph coloring problem instance to be used
    gcp = graphs.GraphColoringProblem(graph, config["hard_constraint_penalty"])

    # define a single objective, minimizing fitness strategy
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

    # create the Individual class based on list:
    creator.create("Individual", list, fitness=creator.FitnessMin)

    # create an operator that randomly returns an integer in the range of participating colors
    toolbox.register("Integers", random.randint, 0, max_colors)

    # create the individual operator to fill up an Individual instance
    toolbox.register(
        "individualCreator", tools.initRepeat, creator.Individual, toolbox.Integers, len(gcp)
    )

    # create the population operator to generate a list of individuals:
    toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

    # fitness calculation: cost of the suggested solution
    def get_cost(individual) -> tuple:
        # NOTE: return a tuple
        return (gcp.get_cost(individual),)

    toolbox.register("evaluate", get_cost)

    # genetic operators
    toolbox.register("select", tools.selTournament, tournsize=2)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register(
        "mutate",
        tools.mutUniformInt,
        low=0,
        up=max_colors,
        indpb=1.0 / len(gcp)
    )

    # create initial population (generation 0):
    population = toolbox.populationCreator(n=config["population_size"])

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", numpy.min)
    stats.register("avg", numpy.mean)

    # define the hall-of-fame object:
    hof = tools.HallOfFame(config["hall_of_fame_size"])

    start_ts = time()
    # perform the Genetic Algorithm flow with elitism:
    population, logbook = elitism.eaSimpleWithElitism(
        population,
        toolbox,
        cxpb=config["p_crossover"],
        mutpb=config["p_mutation"],
        ngen=config["max_generations"],
        stats=stats,
        halloffame=hof,
        verbose=True
    )
    logger.info(f"Genetic algorithm is completed: {round(time() - start_ts, 3)} s")

    # print info for best solution found:
    best_individual = hof.items[0]
    logger.info(f"Best Individual: {best_individual}")
    logger.info(f"Best Fitness: {best_individual.fitness.values[0]}")
    logger.info(f"The number of colors: {gcp.get_color_number(best_individual)}")
    logger.info(f"The number of violations: {gcp.get_violations_count(best_individual)}")
    logger.info(f"The cost: {gcp.get_cost(best_individual)}")

    solution = ScheduleSolution(
        gcp=gcp,
        best_individual=best_individual,
        logbook=logbook
    )

    return solution


def convert_to_dataframe(best_individual, nodes) -> pd.DataFrame:
    day_names = get_days()
    # NOTE: the first and the last intervals are excluded
    time_intervals = get_time_intervals()[1:-1]

    day_time_intervals = list(map(" ".join, product(day_names, time_intervals)))
    day_time_map = dict(enumerate(day_time_intervals))

    schedule_dict = defaultdict(list)
    for color_idx, color in enumerate(best_individual):
        lesson_name = nodes[str(color_idx + 1)]
        schedule_dict[day_time_map[color]].append(lesson_name)

    # TODO: refactor
    schedule_groups = defaultdict(list, {name: [] for name in get_groups()})
    for lessons in schedule_dict.values():
        for group in schedule_groups:
            found = False
            for lesson in lessons:
                cropped_name = "".join(lesson.split(", ")[:3])
                if str(group) in lesson:
                    schedule_groups[group].append(cropped_name)
                    found = True
                    continue

            if not found:
                schedule_groups[group].append(None)

    schedule_df = pd.DataFrame(data=schedule_groups, index=list(schedule_dict.keys()))
    return schedule_df


def main():
    # --- Configuration --- #
    config_fpath = CONFIG_DPATH / "color_graph.yaml"
    config = read_yaml(config_fpath)

    random.seed(config["random_seed"])

    # --- Caching directory --- #
    save_dpath = DATA_DPATH / f"timetable_{get_date_string()}"
    save_dpath.mkdir(parents=True, exist_ok=True)

    # --- Odd week schedule --- #
    graph_odd_week_fpath = GRAPH_DPATH / "1week.pickle"
    nodes_odd_week_fpath = GRAPH_DPATH / "1week_node.json"

    odd_graph = load_graph(graph_odd_week_fpath)
    odd_nodes = read_json(nodes_odd_week_fpath)

    odd_schedule_solution = generate_schedule(odd_graph, config)
    odd_schedule_df = convert_to_dataframe(odd_schedule_solution.best_individual, odd_nodes)

    # --- Odd artifacts caching --- #
    odd_graph_fig = odd_schedule_solution.gcp.get_color_graph(
        odd_schedule_solution.best_individual, figsize=(10, 10)
    )
    color_odd_graph_fpath = save_dpath / "odd_color_graph.jpg"
    odd_graph_fig.savefig(color_odd_graph_fpath)

    odd_fitness_fig = plot_fitness(
        odd_schedule_solution.logbook.select("min"),
        odd_schedule_solution.logbook.select("avg"),
    )
    odd_fitness_fpath = save_dpath / "odd_fitness.jpg"
    odd_fitness_fig.savefig(odd_fitness_fpath)

    # --- Even week schedule --- #
    graph_even_week_fpath = GRAPH_DPATH / "2week.pickle"
    nodes_even_week_fpath = GRAPH_DPATH / "2week_node.json"

    even_graph = load_graph(graph_even_week_fpath)
    even_nodes = read_json(nodes_even_week_fpath)

    even_schedule_solution = generate_schedule(even_graph, config)

    # --- Even artifacts caching --- #
    even_fig = even_schedule_solution.gcp.get_color_graph(
        even_schedule_solution.best_individual, figsize=(10, 10)
    )
    color_even_graph_fpath = save_dpath / "even_color_graph.jpg"
    even_fig.savefig(color_even_graph_fpath)

    even_fitness_fig = plot_fitness(
        even_schedule_solution.logbook.select("min"),
        even_schedule_solution.logbook.select("avg"),
    )
    even_fitness_fpath = save_dpath / "even_fitness.jpg"
    even_fitness_fig.savefig(even_fitness_fpath)

    # --- Schedule dataframe saving --- #
    even_schedule_df = convert_to_dataframe(even_schedule_solution.best_individual, even_nodes)

    schedule_fpath = save_dpath / f"schedule_{get_date_string()}.xlsx"
    with pd.ExcelWriter(schedule_fpath) as writer:
        odd_schedule_df.to_excel(writer, sheet_name="Нечётная неделя", index=False)
        even_schedule_df.to_excel(writer, sheet_name="Чётная неделя", index=False)


if __name__ == "__main__":
    main()
