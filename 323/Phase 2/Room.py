from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Room(Base):
    __tablename__ = "room"
    roomNum = Column("room_num", Integer, nullable=False)
    
    
    def __init__(self, roomNum: Integer):
        self.roomNum = roomNum