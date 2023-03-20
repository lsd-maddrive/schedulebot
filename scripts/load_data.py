import logging
import os

# import click
import numpy as np
import pandas as pd

from schedulebot.db.client import DatabaseClient
from schedulebot.db.models import Qualification
from schedulebot.utils.data import parse_subject_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("database_loading")


# @click.command()
# @click.option("--version", required=True, help="The name of the data folder.")


def main(version: str):
    CURRENT_DPATH = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DPATH, os.pardir))
    DATA_DPATH = os.path.join(PROJECT_ROOT, "data")
    data_version = '2023-02-26'
    src_dpath = os.path.join(DATA_DPATH, data_version)
    fpath = os.path.join(src_dpath, "Teachers+Lessons.csv")
    if DATA_DPATH is None:
        raise ValueError("DATA_DPATH = None")
    dataf = DatabaseClient()
    dataframe = pd.read_csv(fpath, index_col=0)
    parsed_teachers_name = dataframe['TEACHERS'].apply(parse_subject_name).tolist()
    parsed_teachers_name = np.array(parsed_teachers_name).reshape(-1, 2)

    dataframe['name'] = parsed_teachers_name[:, 0]
    dataframe['qualification'] = parsed_teachers_name[:, 1]

    dataf.add_df(df=dataframe['name'], table_name=Qualification.__tablename__)


if __name__ == "__main__":
    main('2023-02-26')
