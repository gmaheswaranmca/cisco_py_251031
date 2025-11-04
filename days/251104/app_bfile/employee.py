class Employee:
    def __init__(self, id, name, job_title, salary):
        self.id = id 
        self.name = name 
        self.job_title = job_title 
        self.salary = salary 
    
    def __repr__(self):
        return f'[id = {self.id}, name = {self.name}, job_title = {self.job_title}, salary = {self.salary}]'
    
    def __str__(self):
        #return f'{self.name}, {self.job_title}'
        return self.__repr__()