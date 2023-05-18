import logging
import os
import random
from time import time

import matplotlib.pyplot as plt
import numpy
import pandas as pd
import seaborn as sns
from deap import base, creator, tools

from schedulebot.genetic import elitism, graphs
from schedulebot.utils.fs import load_graph, read_yaml
from schedulebot.utils.load import get_time_intervals, graph_nodes_1week, remake_str, weekdays

CURRENT_DPATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DPATH, os.pardir))
DATA_DPATH = os.path.join(PROJECT_ROOT, "data")
CONFIG_DPATH = os.path.join(PROJECT_ROOT, "configs")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__file__)


# Genetic Algorithm flow:
def main():
    # read yaml config
    fpath = os.path.join(CONFIG_DPATH, "color_graph.yaml")
    config_constant = read_yaml(fpath)
    logger.info(f"Config: {config_constant}")

    graph_dpath = os.path.join(DATA_DPATH, "graph")
    week1_pickle = os.path.join(graph_dpath, "1week.pickle")
    G = load_graph(week1_pickle)

    # set the random seed:
    random.seed(config_constant['RANDOM_SEED'])

    toolbox = base.Toolbox()

    # create the graph coloring problem instance to be used:
    gcp = graphs.GraphColoringProblem(G, config_constant['HARD_CONSTRAINT_PENALTY'])

    # define a single objective, maximizing fitness strategy:
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

    # create the Individual class based on list:
    creator.create("Individual", list, fitness=creator.FitnessMin)

    # create an operator that randomly returns an integer in the range of participating colors:
    toolbox.register("Integers", random.randint, 0, config_constant['MAX_COLORS'] - 1)

    # create the individual operator to fill up an Individual instance:
    toolbox.register(
        "individualCreator", tools.initRepeat, creator.Individual, toolbox.Integers, len(gcp)
    )

    # create the population operator to generate a list of individuals:
    toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

    # fitness calculation: cost of the suggested olution
    def getCost(individual) -> tuple:
        # NOTE: return a tuple
        return (gcp.getCost(individual),)

    toolbox.register("evaluate", getCost)

    # genetic operators:
    toolbox.register("select", tools.selTournament, tournsize=2)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register(
        "mutate",
        tools.mutUniformInt,
        low=0,
        up=config_constant['MAX_COLORS'] - 1,
        indpb=1.0 / len(gcp)
    )

    # create initial population (generation 0):
    population = toolbox.populationCreator(n=config_constant['POPULATION_SIZE'])

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", numpy.min)
    stats.register("avg", numpy.mean)

    # define the hall-of-fame object:
    hof = tools.HallOfFame(config_constant['HALL_OF_FAME_SIZE'])

    # from time import time

    start_ts = time()
    # perform the Genetic Algorithm flow with elitism:
    population, logbook = elitism.eaSimpleWithElitism(population, toolbox,
                                                      cxpb=config_constant['P_CROSSOVER'],
                                                      mutpb=config_constant['P_MUTATION'],
                                                      ngen=config_constant['MAX_GENERATIONS'],
                                                      stats=stats, halloffame=hof, verbose=True)
    logger.info(f"Genetic algorithm is completed: {round(time() - start_ts, 3)} s")

    # print info for best solution found:
    best = hof.items[0]
    print("-- Best Individual = ", best)
    print("-- Best Fitness = ", best.fitness.values[0])
    print()
    print("number of colors = ", gcp.getNumberOfColors(best))
    print("Number of violations = ", gcp.getViolationsCount(best))
    print("Cost = ", gcp.getCost(best))

    # plot best solution:
    plt.figure(1)
    gcp.plotGraph(best)

    # extract statistics:
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")

    weekday = weekdays()
    color_dicrionary = {}
    index = 1
    for day in weekday:
        for time_slot in get_time_intervals():
            color_dicrionary[index] = day + ' ' + time_slot
            index += 1

    nodes = graph_nodes_1week()
    time_dict = {}
    index = 1
    for color in best:
        study_info = nodes[index]
        if color_dicrionary[color] in time_dict:
            time_dict[color_dicrionary[color]].append(study_info)
        else:
            time_dict[color_dicrionary[color]] = [study_info]
        index += 1
    # print(time_dict, sep='\n')

    group_dict = {'9491': [],
                  '9492': [],
                  '9493': [],
                  '9494': []}

    for value in list(color_dicrionary.values()):
        group_window = ['9491', '9492', '9493', '9494']
        if value in time_dict:
            for subject_info in time_dict[value]:
                for group in group_dict.keys():
                    if group in subject_info.split(", ")[3:]:
                        group_dict[group].append(remake_str(subject_info))
                        group_window.remove(group)
        for group in group_window:
            group_dict[group].append('-')

    schedule = pd.DataFrame(data=group_dict, index=list(color_dicrionary.values()))
    print(schedule)

    # plot statistics:
    plt.figure(2)
    sns.set_style("whitegrid")
    plt.plot(minFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Min / Average Fitness')
    plt.title('Min and Average fitness over Generations')

    plt.show()


if __name__ == "__main__":
    main()
