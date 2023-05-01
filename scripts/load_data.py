import logging
import os

import click
import numpy as np
import pandas as pd

from schedulebot.db.client import DatabaseClient
from schedulebot.db.models import Qualification, Study_interval, Teacher, Time_interval, Weekdays
from schedulebot.utils.data import parse_subject_name
from schedulebot.utils.load import get_time_intervals, split_name, weekdays

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

    db_client = DatabaseClient()

    # --- Qualification --- #
    qualification_df = pd.DataFrame(dataframe['qualification'].unique(), columns=['name'])
    db_client.add_df(df=qualification_df, table_name=Qualification.__tablename__)

    # --- Days --- #
    weekdays_ds = pd.Series(weekdays(), name="name")
    db_client.add_df(df=weekdays_ds, table_name=Weekdays.__tablename__)

    # --- Time interval --- #
    time_interval_df = pd.DataFrame(get_time_intervals(), columns=['interval'])
    db_client.add_df(df=time_interval_df, table_name=Time_interval.__tablename__)

    # --- Study interval --- #
    studydays = db_client.get_id_list(Weekdays)
    studytime = db_client.get_id_list(Time_interval)
    studyweek = []
    for day in studydays:
        for time in studytime:
            studyweek.append(studydays[day - 1])
            studyweek.append(studytime[time - 1])
            record = Study_interval(time_interval_id=studyweek[0], day_id=studyweek[1])
            db_client.add_record(record)
            studyweek = []

    # --- Teachers --- #
    FULL_TEACHERS_NAME = ['Дикун Ирина Александровна', 'Козлова Людмила Петровна',
                          'Королев Виталий Вячеславович', 'Кузнецов Владимир Евгеньевич',
                          'Якупов Олег Эльдусович', 'Буканин Владимир Анатольевич',
                          'Демидович Ольга Васильевна', 'Овдиенко Евгений Николаевич',
                          'Трусов Александр Александрович', 'Трусов Александр Олегович',
                          'Леута Алексей Александрович', 'Мирошников Александр Николаевич',
                          'Амбросовская Елена Борисовна', 'Лукичев Андрей Николаевич',
                          'Михайлов Данил Павлович', 'Копычев Михаил Михайлович',
                          'Игнатович Юлия Васильевна', 'Скороходов Дмитрий Алексеевич',
                          'Вейнмейстер Андрей Викторович', 'Филатова Екатерина Сергеевна',
                          'Богданова Светлана Михайловна', 'Федоркова Анастасия Олеговна',
                          'Гречухин Михаил Николаевич']
    splited_names = split_name(FULL_TEACHERS_NAME)

    first_name = splited_names[1]
    middle_name = splited_names[0]
    last_name = splited_names[2]
    lessons_one_week = pd.read_csv(fpath, usecols=['TEACHERS_LESSONS_ONE_WEEK'])
    lessons_one_week = lessons_one_week['TEACHERS_LESSONS_ONE_WEEK'].tolist()

    qualification_id = []
    i = 0
    while i < len(dataframe['qualification']):
        if dataframe.iloc[i, 2] == "professor":
            qualification_id.append(1)
        elif dataframe.iloc[i, 2] == "assistant":
            qualification_id.append(2)
        i += 1
    cash = []
    i = 0
    while i < len(first_name):
        cash.append(first_name[i])
        cash.append(middle_name[i])
        cash.append(last_name[i])
        cash.append(lessons_one_week[i])
        cash.append(qualification_id[i])
        record = Teacher(first_name=cash[0],
                         middle_name=cash[1],
                         last_name=cash[2],
                         load_hours=cash[3],
                         qualification_id=cash[4])
        db_client.add_record(record)
        i += 1
        cash = []


if __name__ == "__main__":
    main()
