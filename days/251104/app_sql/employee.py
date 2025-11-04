from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    job_title = Column(String(150), nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f'[id = {self.id}, name = {self.name}, job_title = {self.job_title}, salary = {self.salary}]'
 