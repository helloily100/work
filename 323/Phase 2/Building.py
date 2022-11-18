from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Building(Base):
    __tablename__ = "building"
    buildingName = Column("building_name", String, nullalbe=False)
    
    def __init__(self, buildingName: String):
        self.buildingName = buildingName