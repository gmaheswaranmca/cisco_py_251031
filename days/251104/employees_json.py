import json 

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
    
    def to_dict(self):
        return {'id' : self.id, 'name' : self.name, 'job_title' : self.job_title, 
                'salary' : self.salary}
    
    @staticmethod 
    def from_dict(employee_dict):
        return Employee(employee_dict['id'], employee_dict['name'],
                        employee_dict['job_title'], employee_dict['salary'])


employees = [Employee(101,'Pratik', 'Software Engineer', 56000),
    Employee(102,'Abhishek', 'Software Automation Engineer', 40000),
    Employee(103,'Rishabh', 'Software Automation Engineer', 99000),
    Employee(104,'Nihar', 'Software Automation Engineer', 99),
    Employee(105,'Divya', 'Business Analyst', 45000)]

file_name = 'employees_db.json'

print('To save employees into json file...')
with open(file_name, 'w') as out_file:
    employees_dict = [employee.to_dict() for employee in employees]
    json.dump(employees_dict, out_file)
    print('Employees saved')

print('Access employees from json file...')
with open(file_name, 'r') as in_file:
    queried_employees_dict = json.load(in_file)
    print('The queried employees from file:')
    queried_employees = [Employee.from_dict(employee_dict) for employee_dict in queried_employees_dict]
    print(queried_employees)

    

