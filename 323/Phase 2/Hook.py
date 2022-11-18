'''
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Hook(Base):
    __tablename__ = "hook"
    hook = Column("hook", String(40), nullable=False)
    
    def __init__(self, hook: String):
        self.hook = hook
'''
from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint
from sqlalchemy.orm import relationship

from orm_base import Base
from Unknown import Unknown

class Hook(Base):
    __tablebname__ = "hooks"
    hook = Column('hook', String(100), nullable=False)
    doors_list: [Unknown] = relationship("Unknown", back_populates="hook", viewonly=False)
    def __init__(self, hook: String):
        self.hook = hook
        self.doors_list = []

    def add_door(self, door):
        # make sure this genre is non already on the list.
        for next_door in self.doors_list:
            if next_door == door:
                return
        # Create an instance of the junction table class for this relationship.
        unknown = Unknown(self, door)
        # Update this move to reflect that we have this genre now.
        door.hooks_list.append(unknown)
        # Update the genre to reflect this movie.
        self.doors_list.append(unknown)
