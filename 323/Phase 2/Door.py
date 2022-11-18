'''
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Door(Base):
    __tablename__ = "door"
    doorType = Column("door_type", String(40), nullable=False)
    
    def __ini__(self, doorType: String):
        self.doorType = doorType
'''
from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint
from sqlalchemy.orm import relationship

from orm_base import Base
from Unknown import Unknown

class Door(Base):
    __tablebname__ = "doors"
    door_type = Column('door_type', String(100), nullable=False)
    hooks_list : [Unknown] = relationship("Unknown", back_populates="door", viewonly=False)
    def __init__(self, door_type: String):
        self.door_type = door_type
        self.hooks_list = []

    def add_hook(self, hook):
        for next_hook in self.hooks_list:
            if next_hook == hook:
                return
        # Create an instance of the junction table class.
        unknown = Unknown(hook, self)
        # add that new instance to the list of genres that the Movie keeps.
        hook.doors_list.append(unknown)
        # add that new instance to the list of movies that this genre keeps.
        self.hooks_list.append(unknown)

