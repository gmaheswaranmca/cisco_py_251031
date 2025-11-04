'''
    json file persistence storage 
    using std module json
'''
import json
import os
from employee import Employee

FILE_NAME = 'employees_db.json'
def read_employees():
    '''
        reads employees from db 
    '''
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, 'r') as input_file:
        queried_employees_dict = json.load(input_file)
        queried_employees = [Employee.from_dict(employee_dict) for employee_dict in queried_employees_dict]
        return queried_employees

def write_employees(employees):
    '''
        writes employees into db
    '''
    with open(FILE_NAME, 'w') as output_file:
        employees_dict = [employee.to_dict() for employee in employees]
        json.dump(employees_dict, output_file)
