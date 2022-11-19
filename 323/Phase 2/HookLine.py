from sqlalchemy import Column, Integer, Identity, Float, \
    String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from orm_base import Base

class HookLine(Base): 
  __tablename__ = "hook_lines"
  
 def __init__(self):
