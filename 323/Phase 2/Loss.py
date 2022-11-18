from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Loss(Base):
    __tablename__ = "loss"
    reportLossDate = Column("report_loss_date", Date, nullable=False)
    
    def __int__(self, reportLossDate: Date):
        self.reportLossDate = reportLossDate