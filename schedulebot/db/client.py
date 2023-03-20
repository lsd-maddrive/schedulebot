import logging
import os

import sqlalchemy as sql
from dotenv import load_dotenv


class DatabaseClient:
    key = 'DB_DPATH'

    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)
        load_dotenv()
        self.db_dpath = os.getenv(self.key)
        if self.db_dpath is None:
            raise ValueError("DB_DPATH = None")
        os.makedirs(self.db_dpath, exist_ok=True)
        self.sqlite_filepath = os.path.join(self.db_dpath, 'data.db')
        engine = sql.create_engine(f"sqlite:///{self.sqlite_filepath}")
        self._session = sql.sessionmaker(bind=engine)
        self._logger.info(f"The engine {self.sqlite_filepath} was created successfully")
