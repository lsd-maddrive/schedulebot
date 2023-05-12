import logging
import os

import click
import pandas as pd

from schedulebot.db.client import DatabaseClient
from schedulebot.db.models import (
    Group,
    GroupSubject,
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
from schedulebot.utils.load import create_groups, eng_room_type, get_time_intervals, room_types, weekdays

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
    room_type_map = eng_room_type()
    for room, subject_type in zip(room_df['room'], room_df['subject_type']):
        building, floor = room[:2]
        number = room[2:]
        subject_type = room_type_map[subject_type]
        type_id = db_client.get_id(RoomType, [RoomType.name.like(subject_type)])
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
        record = SubjectRoom(subject_id=subject_id, room_id=room_id)
        db_client.add_record(record)

    mixed_id = db_client.get_id(RoomType, conditions=[RoomType.name.like('mixed')])
    mixed_room_id = db_client.get_filter_ids(Room, conditions=[Room.type_id.like(mixed_id)])
    for subject_type in subject_ds:
        subject_id = db_client.get_id(Subject, conditions=[Subject.name.like(subject_type)])
        subject_type = subject_type.split()[-1]
        if subject_type != 'лаб.':
            room_type = room_type_map[subject_type]
            type_id = db_client.get_id(RoomType, [RoomType.name.like(room_type)])
            rooms_id = db_client.get_filter_ids(Room, conditions=[Room.type_id.like(type_id)])
            for room_id in rooms_id:
                record = SubjectRoom(subject_id=subject_id, room_id=room_id)
                db_client.add_record(record)

            for id in mixed_room_id:
                record = SubjectRoom(subject_id=subject_id, room_id=id)
                db_client.add_record(record)

    # --- Groups --- #
    groups = pd.DataFrame(create_groups(), columns=['name'])
    db_client.add_df(groups, table_name=Group.__tablename__)

    # --- Group subject --- #
    fpath_room = os.path.join(src_dpath, "Subjects+Groups.csv")
    subject_group_df = pd.read_csv(fpath_room, index_col=0)

    subjects = subject_group_df["subjects"].values
    groups_info = subject_group_df.apply(lambda row: row[row == 1].index.values, axis=1).values
    for subject, group_list in zip(subjects, groups_info):
        subject_id = db_client.get_id(Subject, conditions=[Subject.name.like(subject)])
        for value in group_list:
            group_id = db_client.get_id(Group, conditions=[Group.name.like(int(value))])
            record = GroupSubject(group_id=group_id, subject_id=subject_id)
            db_client.add_record(record)


if __name__ == "__main__":
    main()
