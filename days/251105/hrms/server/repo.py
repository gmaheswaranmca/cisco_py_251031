from server.models import db, Employee

def read_all_employees():
    employees = db.session.query(Employee).all()
    return employees

def add_employee(employee):
    db.session.add(employee)
    db.session.commit()
    #print('Employee Added Successfully')

def search_employee(id): 
    employee = db.session.query(Employee).filter_by(id = id).first()
    return employee
 
def update_employee(id, salary):
    old_employee = search_employee(id)

    if not old_employee: 
        #print('Employee Not Found.')
        return
    
    old_employee.salary = salary
    db.session.commit()
    #print('Employee Updated Successfully')        
    

def delete_employee(id):
    old_employee = search_employee(id)

    if not old_employee: 
        #print('Employee Not Found.')
        return
    
    db.session.delete(old_employee)
    db.session.commit()
    #print('Employee Deleted Successfully')