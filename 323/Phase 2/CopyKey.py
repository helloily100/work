from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class CopyKey(Base):
    __tablename__ = "copy_key"
    keyNumber = Column("key_number", Integer, nullable=False)
    issuedDate = Column("issued_date", Date, nullable=False)
    issuedTime = Column("issued_time", Time, nullable=False)
    
    def __int__(self, keyNumber: Integer, issuedDate: Date, issuedTime: Time):
        self.keyNumber = keyNumber
        self.issuedDate = issuedDate
        self.issuedTime = issuedTime