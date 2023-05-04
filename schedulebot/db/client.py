from typing import List

import logging
import os

import pandas as pd
import sqlalchemy as sql
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from schedulebot.db.models import metadata


class DatabaseClient():
    """Class create a path and engine to put SQL data in folder."""

    key = 'DB_DPATH'

    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)

        load_dotenv()
        self.db_dpath = os.getenv(self.key)
        if self.db_dpath is None:
            raise ValueError("DB_DPATH = None")
        os.makedirs(self.db_dpath, exist_ok=True)

        self.sqlite_filepath = os.path.join(self.db_dpath, 'data.db')
        self._engine = sql.create_engine(f"sqlite:///{self.sqlite_filepath}")

        self._session = sessionmaker(bind=self._engine)

        metadata.create_all(self._engine)

        self._logger.info(f"The engine {self.sqlite_filepath} was created successfully")

    def add_df(self, df: pd.DataFrame, table_name: str, if_exist: str = "append"):
        """Creates a file and adds data from df to it

        Parameters
        ----------
        df : DataFrame
            data
        table_name : str
            table title
        if_exist : str, optional
            if the table already exists, insert new values to the existing table,
            by default "append"
        """
        with self._engine.begin() as connection:
            df.to_sql(name=table_name, con=connection, if_exists=if_exist, index=False)

    def get_id_list(self, table) -> List[int]:
        with self._session() as session:
            ids = [val[0] for val in session.query(table.id).distinct()]
        return ids

    def add_record(self, record):
        with self._session() as session:
            session.add(record)
            session.commit()

    def get_id(self, table, column, quality) -> List[int]:
        with self._session() as session:
            x = [val[0] for val in session.query(table.id).filter(column == quality).all()]
        return x
