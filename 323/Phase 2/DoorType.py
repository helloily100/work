from sqlalchemy import Column, Integer, Identity, Float, \
    String, Date, UniqueConstraint
from sqlalchemy.orm import relationship

from orm_base import Base


class DoorType(Base):
    __tablebname__ = "door_type"
    name = Column('name', Date, primary_key= True, nullable=False)

    def __init__(self, name: String):
        self.name = name
