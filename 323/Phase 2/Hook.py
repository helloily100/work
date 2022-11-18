from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Hook(Base):
    __tablename__ = "hook"
    hook = Column("hook", String(40), nullable=False)
    
    def __init__(self, hook: String):
        self.hook = hook