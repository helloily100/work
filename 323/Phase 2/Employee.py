from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Emplyoee(Base):
    __tablename__ = "employee"
    name = Column("name", String(40), nullable=False)
    emplyoeeID = Column("employee_id", Integer, nullable=False)
    
def _init_(self, name: String, employeeID: Integer):
    self.name = name
    self.employeeID = employeeID 