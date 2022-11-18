from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
from Enrollment import Enrollment


class Student(Base):
    __tablename__ = "student"
    last_name = Column("last_name", String(40), nullable=False)
    first_name = Column("first_name", String(40), nullable=False)
    id = Column("id", Integer, nullable=False, primary_key=True)

    section_list: [Enrollment] = relationship("Enrollment", back_populates="student", viewonly=False)

    def __int__(self, last_name: String, first_name: String, id: Integer):
        self.last_name = last_name
        self.first_name = first_name
        self.id = id
        self.section_list = []

    def add_section(self, section):
        for next_section in self.section_list:
            if next_section == section:
                return

        enrollment = Enrollment(section, self)
        section.student_list.append(enrollment)
        self.section_list.append(enrollment)

    def __str__(self):
        return "Student: {last_name, first_name}".format(last_name=self.last_name, first_name=self.first_name)
