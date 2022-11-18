from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base


class Enrollment(Base):
    __tablename__ = "enrollment"
    # grade = Column("grade", String(4), nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True, nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'), primary_key=True, nullable=False)

    student = relationship("Student", back_populates='section_list')
    section = relationship("Section", back_populates='student_list')

    def __init__(self, section, student):
        self.section_id = section.id
        self.student_id = student.id
        self.student = student
        self.section = section
