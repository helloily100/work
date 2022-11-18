from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Door(Base):
    __tablename__ = "door"
    doorType = Column("door_type", String(40), nullable=False)
    
    def __int__(self, doorType: String):
        self.doorType = doorType