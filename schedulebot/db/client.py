import logging
import os

import sqlalchemy as sql
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from schedulebot.db.models import metadata


class DatabaseClient():
    """Class create a path and engine to put SQL data in folder"""
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
        self._logger.info(f"The engine {self.sqlite_filepath} was created successfully")

    def add_df(self, df, table_name, if_exist="append"):
        with self._engine.begin() as connection:
            metadata.create_all(self._engine)
            df.to_sql(name=table_name, con=connection, if_exists='append', index=False)
