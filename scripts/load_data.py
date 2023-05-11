import logging
import os

import click
import pandas as pd

from schedulebot.db.client import DatabaseClient
from schedulebot.db.models import (
    Qualification,
    Room,
    RoomType,
    StudyInterval,
    Subject,
    SubjectRoom,
    Teacher,
    TeacherSubject,
    TimeInterval,
    Weekdays,
)
from schedulebot.utils.load import get_time_intervals, room_types, weekdays

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
    dataframe = pd.read_csv(fpath)

    db_client = DatabaseClient()

    # --- Qualification --- #
    qualification_data = dataframe["TEACHERS"].str.split().str[-1].unique()
    qualification_df = pd.DataFrame(qualification_data, columns=['name'])
    db_client.add_df(df=qualification_df, table_name=Qualification.__tablename__)

    # --- Days --- #
    weekdays_ds = pd.Series(weekdays(), name="name")
    db_client.add_df(df=weekdays_ds, table_name=Weekdays.__tablename__)

    # --- Time interval --- #
    time_interval_df = pd.DataFrame(get_time_intervals(), columns=['interval'])
    db_client.add_df(df=time_interval_df, table_name=TimeInterval.__tablename__)

    # --- Study interval --- #
    study_days = db_client.get_id_list(Weekdays)
    time_interval = db_client.get_id_list(TimeInterval)
    for day in study_days:
        for time in time_interval:
            record = StudyInterval(time_interval_id=time, day_id=day)
            db_client.add_record(record)

    # --- Teachers --- #
    full_teachers_names = dataframe['TEACHERS'].tolist()
    lessons_one_week = dataframe['TEACHERS_LESSONS_ONE_WEEK'].tolist()

    for teacher_info, teacher_load in zip(full_teachers_names, lessons_one_week):
        middle_name, first_name, last_name, qualification = teacher_info.split()
        quality_id = db_client.get_id(Qualification, [Qualification.name.like(qualification)])
        record = Teacher(middle_name=middle_name,
                         first_name=first_name,
                         last_name=last_name,
                         qualification_id=quality_id,
                         load_hours=teacher_load)
        db_client.add_record(record)

    # --- Subject --- #
    fpath_sub = os.path.join(src_dpath, "Subjects+Teachers.csv")
    subject_df = pd.read_csv(fpath_sub, index_col=0)
    subject_ds = pd.Series(subject_df["subjects"], name="name")
    db_client.add_df(subject_ds, table_name=Subject.__tablename__)

    # --- Teacher subject --- #
    time_interval = subject_df["subjects"].values
    teachers_info = subject_df.apply(lambda row: row[row == 1].index.values, axis=1).values

    for list_names, subject in zip(teachers_info, time_interval):
        subject_index = db_client.get_id(Subject, [Subject.name.like(subject)])
        for name in list_names:
            middle_name, first_name, last_name = name.split()[:-1]
            conditions = [
                Teacher.first_name.like(first_name),
                Teacher.middle_name.like(middle_name),
                Teacher.last_name.like(last_name)
            ]
            teacher_index = db_client.get_id(Teacher, conditions)
            record = TeacherSubject(teacher_id=teacher_index, subject_id=subject_index)
            db_client.add_record(record)

    # --- Room type --- #
    room_df = pd.DataFrame(room_types(), columns=['name'])
    db_client.add_df(df=room_df, table_name=RoomType.__tablename__)

    # --- Room --- #
    fpath_room = os.path.join(src_dpath, "Room+Subject_Type.csv")
    room_df = pd.read_csv(fpath_room, index_col=0)
    for room, subject_type in zip(room_df['room'], room_df['subject_type']):
        building = room[0]
        floor = room[1]
        number = room[2:]
        if subject_type == 'пр.':
            room_type = 'practice'
        if subject_type == 'лек.':
            room_type = 'lecture'
        if subject_type == 'лаб.':
            room_type = 'lab'
        if subject_type == 'mixed':
            room_type = 'mixed'
        type_id = db_client.get_id(RoomType, [RoomType.name.like(room_type)])
        record = Room(name=room,
                      building=building,
                      floor=floor,
                      number=number,
                      type_id=type_id)
        db_client.add_record(record)

    # --- Subject room --- #
    fpath_room = os.path.join(src_dpath, "Lab+Room.csv")
    subject_room_df = pd.read_csv(fpath_room, index_col=0)
    labs = subject_room_df["lab"]
    rooms = subject_room_df["room"]
    for x, lab in zip(rooms, labs):
        room_id = db_client.get_id(Room, conditions=[Room.name.like(x)])
        lab = lab + ' лаб.'
        subject_id = db_client.get_id(Subject, conditions=[Subject.name.like(lab)])
        # subject_ds
        record = SubjectRoom(subject_id=subject_id, room_id=room_id)
        db_client.add_record(record)

    """lecture_room_id = db_client.get_id(RoomType, conditions=[RoomType.name.like('lecture')])
    rooms_id = db_client.get_id(Room, conditions=[Room.name.like(lecture_room_id)])
    # список id аудиторий с лекциями
    for id in rooms_id:
        subject_df['subjects']"""
    test = db_client.get_id(Subject, conditions=[Subject.name.like('лек.')])
    print(test)


if __name__ == "__main__":
    main('2023-05-05')
