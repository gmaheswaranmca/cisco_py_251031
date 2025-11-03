from employee import Employee 
from repo import add_employee, search_employee, update_employee, delete_employee, employees
add_employee(Employee(101,'Pratik', 'Software Engineer', 56000))
add_employee(Employee(102,'Abhishek', 'Software Automation Engineer', 40000))
add_employee(Employee(103,'Rishabh', 'Software Automation Engineer', 99000))
add_employee(Employee(104,'Nihar', 'Software Automation Engineer', 99))
add_employee(Employee(105,'Divya', 'Business Analyst', 45000))

print(employees)

emp_index = search_employee(104)
if emp_index != -1:
    print('Searched employee:', employees[emp_index])
else:
    print('Empoloyee Not Found.')

update_employee(104,99200)
print(employees)

add_employee(Employee(106,'Mahesh', 'Python Trainer', 4200))
print(employees)
delete_employee(106)
print(employees)