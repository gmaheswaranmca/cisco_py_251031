from db_setup import session, Employee

def read_all_employees():
    employees = session.query(Employee).all()
    return employees

def add_employee(employee):
    session.add(employee)
    session.commit()
    print('Employee Added Successfully')

def search_employee(id): 
    employee = session.query(Employee).filter_by(id = id).first()
    return employee
 
def update_employee(id, salary):
    old_employee = search_employee(id)

    if not old_employee: 
        print('Employee Not Found.')
        return
    
    old_employee.salary = salary
    session.commit()
    print('Employee Updated Successfully')        
    

def delete_employee(id):
    old_employee = search_employee(id)

    if not old_employee: 
        print('Employee Not Found.')
        return
    
    session.delete(old_employee)
    session.commit()
    print('Employee Deleted Successfully')