import logging
import os

import sqlalchemy as sql
from dotenv import load_dotenv


class DatabaseClient():
    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)

        load_dotenv()
        key = 'DB_DPATH'
        self.DB_DPATH = os.getenv(key)

        if self.DB_DPATH is None:
            raise ValueError("DB_DPATH = None")
        else:
            os.makedirs(self.DB_DPATH, exist_ok=True)
            PATH_TO_DB = os.path.join(self.DB_DPATH, 'data.db')
        self.sqlite_filepath = PATH_TO_DB
        engine = sql.create_engine(f"sqlite:///{self.sqlite_filepath}")
        self._session = sql.sessionmaker(bind=engine)
