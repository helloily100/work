from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, Identity
from sqlalchemy.orm import relationship
from orm_base import Base
from Enrollment import Enrollment


class Section(Base):
    __tablename__ = "section"
    department_name = Column('department_name', String(20), nullable=False)
    course_name = Column('course_name', String(40), nullable=False)
    section_number = Column('section_number', Integer, nullable=False)
    semester = Column('semester', String(40), nullable=False)
    year = Column('year', Integer, nullable=False)
    id = Column('id', Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)

    table_args = (UniqueConstraint('department_name', 'course_name', 'section_number', 'semester', 'year',
                                   name='semester_uk_01'))

    student_list: [Enrollment] = relationship("Enrollment", back_populates="section", viewonly=False)

    def __init__(self, department_name: String, course_name: String, section_number: Integer, semester: String,
                 year: Integer, id: Integer):
        self.department_name = department_name
        self.course_name = course_name
        self.section_number = section_number
        self.semester = semester
        self.year = year
        self.id = id
        self.student_list = []

    def add_student(self, student):
        for next_student in self.student_list:
            if next_student == student:
                return
        enrollment = Enrollment(self, student)
        student.section_list.append(enrollment)
        self.student_list.append(enrollment)
