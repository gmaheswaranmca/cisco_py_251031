from server.models import db, Employee
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .exc import EmployeeNotFoundError, EmployeeAlreadyExistError, DatabaseError
from .log import logging 

def read_all_employees():
    employees = db.session.query(Employee).all()
    logging.info("Read all employees.")
    return employees

def add_employee(employee):
    try:
        db.session.add(employee)
        db.session.commit()
        logging.info('Employee Added Successfully')
    except IntegrityError as ex:
        db.session.rollback()
        logging.error("Duplicate employee id:%s",ex)
        raise EmployeeAlreadyExistError(f"Employee id={employee['id']} exists already.")
    except SQLAlchemyError as ex:
        db.session.rollback()
        logging.error("Database error in creating employee:%s",ex)
        raise DatabaseError("Error in creating employee.")
    
def search_employee(id): 
    employee = db.session.query(Employee).filter_by(id = id).first()
    logging.info("Read employee for given id.")
    return employee
 
def update_employee(id, salary):
    old_employee = search_employee(id)

    if not old_employee: 
        logging.info(f"Employee not found {id}.")
        return
    
    old_employee.salary = salary
    db.session.commit()
    logging.info("Employee salary updated.")

def delete_employee(id):
    old_employee = search_employee(id)

    if not old_employee: 
        logging.info(f"Employee not found {id}.")
        return
    
    db.session.delete(old_employee)
    db.session.commit()
    logging.info('Employee Deleted Successfully')