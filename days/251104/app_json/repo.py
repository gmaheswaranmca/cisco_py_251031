import db_json as db 
from log import logging 

employees = db.read_employees() #employee is object of attr (id, name, job_title, salary)
# list of objects -> list of dict -> save to file
# read from file -> list of dict -> list of objs

def add_employee(employee):
    try:
        employees.append(employee)
        logging.debug(f'Employee {employee} added to list')
        db.write_employees(employees)
        logging.debug(f'Employees written to the file')
        logging.info('Employee Added Successfully')
    except Exception as ex:
        logging.exception(f'Employee Added Failed. {ex}')

def search_employee(id): 
    I = 0
    for employee in employees: 
        if employee.id == id:
            logging.info('Employee Exist')
            return I
        I += 1
    logging.info('Employee Not xist')
    return -1 
 
def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employee = employees[index]
        employee.salary = salary
        db.write_employees(employees)
        logging.info('Employee Updated Successfully')
    else: 
        logging.info('Employee Not Found.')

def delete_employee(id):
    index = search_employee(id) 
    if index != -1:
        employees.pop(index)
        db.write_employees(employees)
        logging.info('Employee Deleted Successfully')
    else: 
        logging.info('Employee Not Found.')