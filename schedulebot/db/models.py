from sqlalchemy import Column, ForeignKey, Integer, MetaData, String
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


class Time_interval(Model):
    """Table with time intervals"""

    __tablename__ = "time_interval"

    id = Column(Integer, primary_key=True)
    interval = Column(String(30), nullable=False)


class Study_interval(Model):
    """Table with study interval"""

    __tablename__ = "study_interval"

    id = Column(Integer, primary_key=True)
    time_interval_id = Column(ForeignKey('time_interval.id'))
    day_id = Column(ForeignKey('weekday.id'))
