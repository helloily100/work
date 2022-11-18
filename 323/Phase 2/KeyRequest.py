from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class KeyRequest(Base):
    __tablename__ = "key_request"
    room = Column("room", Integer, nullable=False)
    requestDate = Column("request_date", Date, nullable=False)
    
    def _int__ (self, room: Integer, requestDate: Date):
        self.room = room
        self.requestDate = requestDate
        
        