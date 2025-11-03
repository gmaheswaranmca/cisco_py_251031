import pickle 



employees = [] #employee is object of attr (id, name, job_title, salary)
# list of objects -> list of dict -> save to file
# read from file -> list of dict -> list of objs

def add_employee(employee):
    employees.append(employee)
    print('Employee Added Successfully')

def search_employee(id): 
    I = 0
    for employee in employees: 
        if employee.id == id:
            return I
        I += 1
    return -1 
 
def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employee = employees[index]
        employee.salary = salary
        print('Employee Updated Successfully')
    else: 
        print('Employee Not Found.')

def delete_employee(id):
    index = search_employee(id) 
    if index != -1:
        employees.pop(index)
        print('Employee Deleted Successfully')
    else: 
        print('Employee Not Found.')