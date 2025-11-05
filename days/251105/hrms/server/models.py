from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    job_title = db.Column(db.String(150), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'[id = {self.id}, name = {self.name}, job_title = {self.job_title}, salary = {self.salary}]'
        
    def to_dict(self):
        return {'id' : self.id, 'name' : self.name, 'job_title' : self.job_title, 
            'salary' : self.salary} 