from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Return(Base):
    __tablename__ = "return"
    reportReturnDate = Column("report_return_date", Date, nullable=False)
    
    def __int__(self, reportReturnDate: Date):
        self.reportReturnDate = reportReturnDate