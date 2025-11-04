from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Float, create_engine

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    job_title = Column(String(150), nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f'[id = {self.id}, name = {self.name}, job_title = {self.job_title}, salary = {self.salary}]'
    
# setup database
engine = create_engine('sqlite:///employees_db.sqlite', echo=True) #create database if not exist 
Base.metadata.create_all(engine) # create the tables for model classes

# setup things for transactions (crud ops)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# crud ops
'''
dravid = Employee(name = 'Dravid', job_title = 'Old Coach', salary = 1200)
session.add(dravid)
session.commit()
'''

'''
jaiswal = Employee(name = 'Jaiswal', job_title = 'Batsman', salary = 20000)
session.add(jaiswal)

abhishek = Employee(name = 'abhishek', job_title = 'No 1 T20 Batsman', salary = 1000000)
session.add(abhishek)
session.commit()

employees = session.query(Employee).all()
print(employees)

abhi = session.query(Employee).filter_by(name = 'abhishek').first()
print(abhi)

abhishek.salary = 20001
session.commit()
'''

mahesh = Employee(name='Mahesh', job_title='Trainer', salary=4200)
session.add(mahesh)
session.commit()

employees = session.query(Employee).all()
print(employees)

session.delete(mahesh)
session.commit()

employees = session.query(Employee).all()
print(employees)