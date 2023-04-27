import logging
import os

import click
import numpy as np
import pandas as pd

from schedulebot.db.client import DatabaseClient
from schedulebot.db.models import Qualification, Time_interval
from schedulebot.utils.data import parse_subject_name
from schedulebot.utils.load import get_time_intervals

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("database_loading")
CURRENT_DPATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DPATH, os.pardir))
DATA_DPATH = os.path.join(PROJECT_ROOT, "data")


@click.command()
@click.option("--version", required=True, help="The name of the data folder.")
def main(version: str):
    data_version = version
    src_dpath = os.path.join(DATA_DPATH, data_version)
    fpath = os.path.join(src_dpath, "Teachers+Lessons.csv")
    dataframe = pd.read_csv(fpath, usecols=['TEACHERS'])

    parsed_teachers_name = dataframe['TEACHERS'].apply(parse_subject_name).tolist()
    parsed_teachers_name = np.array(parsed_teachers_name).reshape(-1, 2)

    dataframe['name'] = parsed_teachers_name[:, 0]
    dataframe['qualification'] = parsed_teachers_name[:, 1]

    df_client = pd.DataFrame(dataframe['qualification'].unique(), columns=['name'])
    df_time_interval = pd.DataFrame(get_time_intervals(), columns=['interval'])

    db_client = DatabaseClient()
    db_client.add_df(df=df_client, table_name=Qualification.__tablename__)
    db_client.add_df(df=df_time_interval, table_name=Time_interval.__tablename__)


if __name__ == "__main__":
    main()
