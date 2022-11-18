from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class KeyStatus(Base):
    __tablename__ = "key_status"
    isLoss = Column("is_loss", Boolean, nullable=False)
    
    def __init__(self, isLoss: Boolean):
        self.isLoss = isLoss