from sqlalchemy import Column, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Model = declarative_base(metadata=metadata)


class qualification(Model):
    """Table with model qualification"""

    __tablename__ = "qualification"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    def __repr__(self):
        return(f"<Qualification(id={self.id}, name={self.name})>")
