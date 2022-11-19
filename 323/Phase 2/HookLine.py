from sqlalchemy import Column, Integer, Identity, Float, \
    String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from orm_base import Base

#junction table that connects hook and door class
class HookLine(Base): 
  __tablename__ = "hook_lines"
  
 def __init__(self):
