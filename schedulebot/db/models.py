from sqlalchemy import Column, Float, ForeignKey, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Model = declarative_base(metadata=metadata)


class Qualification(Model):
    """Table with values/types qualification"""

    __tablename__ = "qualification"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    def __repr__(self):
        return(f"<Qualification(id={self.id}, name={self.name})>")


class Weekdays(Model):
    """Table with the days from Monday to Saturday"""

    __tablename__ = "weekday"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class TimeInterval(Model):
    """Table with time intervals"""

    __tablename__ = "time_interval"

    id = Column(Integer, primary_key=True)
    interval = Column(String(30), nullable=False)


class StudyInterval(Model):
    """Table with study interval"""

    __tablename__ = "study_interval"

    id = Column(Integer, primary_key=True)
    time_interval_id = Column(ForeignKey('time_interval.id'))
    day_id = Column(ForeignKey('weekday.id'))


class Teacher(Model):
    """Table with names of teachers and load hours"""

    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    middle_name = Column(String(30), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    load_hours = Column(Float, nullable=False)
    qualification_id = Column(ForeignKey('qualification.id'))


class Subject(Model):
    """Table with subjects"""

    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class TeacherSubject(Model):
    """Table with teachers subjects"""

    __tablename__ = "teachers_subjects"

    id = Column(Integer, primary_key=True)
    teacher_id = Column(ForeignKey("teachers.id"))
    subject_id = Column(ForeignKey("subjects.id"))


class RoomType(Model):
    """Table with room type"""

    __tablename__ = "room_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class Room(Model):
    """Table with university's rooms"""

    __tablename__ = "room"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    building = Column(String, nullable=False)
    floor = Column(Integer, nullable=False)
    number = Column(String, nullable=False)
    type_id = Column(ForeignKey("room_type.id"))


class SubjectRoom(Model):
    """Table with university's subject rooms"""

    __tablename__ = "subject_room"

    id = Column(Integer, primary_key=True)
    subject_id = Column(ForeignKey('subjects.id'))
    room_id = Column(ForeignKey('room.id'))


class Group(Model):
    """Table with groups"""

    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)


class GroupSubject(Model):
    """Table with groups and subjects"""

    __tablename__ = 'group_subject'

    id = Column(Integer, primary_key=True)
    group_id = Column(ForeignKey('group.id'))
    subject_id = Column(ForeignKey('subjects.id'))
