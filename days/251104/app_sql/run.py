from employee import Employee 
import repo

def menu():
    option_str = '''Options are
1 - Create Employee
2 - Search Employee
3 - Update Salary 
4 - Delete Employee
5 - List All Employees
6 - Exit
Your Choice:'''
    choice = int(input(option_str))

    if choice == 1:
        id = input('ID:')
        name = input('Name:')
        job_title = input('Job Title:')
        salary = input('Salary:')
        
        old_employee = repo.search_employee(id)
        if old_employee:
            print('ID already exist.')
        else:
            repo.add_employee(Employee(id=id, name=name, job_title=job_title, salary=salary))
            print(f'Employee {name} added successfully')
    elif choice == 2:
        id = input('ID:')
        old_employee = repo.search_employee(id)
        if not old_employee:
            print('Employee Not Found.')
        else:
            print(old_employee)
    elif choice == 3:
        id = input('ID:')
        old_employee = repo.search_employee(id)
        if not old_employee:
            print('Employee Not Found.')
        else:
            print(old_employee)
            new_salary = input('New Salary:')
            repo.update_employee(id, new_salary)
            print(f'Employee {old_employee.name} salary updated successfully')
    elif choice == 4:
        id = input('ID:')
        old_employee = repo.search_employee(id)
        if not old_employee:
            print('Employee Not Found.')
        else:
            print(old_employee)
            if input('Are you sure to delete(y/n)?').upper() == 'Y':
                repo.delete_employee(id)
                print(f'Employee deleted successfully')
    elif choice == 5:
        employees = repo.read_all_employees()
        if len(employees) == 0:
            print('No employee exist.')
        else:
            print('List of Employees:')
            for employee in employees:
                print(employee)
    elif choice == 6:
        print('Thank you for using the application')
    else:
        print('No such option is available. Give proper option.')

    return choice 

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()
    print('End of application.')

menus()

'''
repo.add_employee(Employee(101,'Pratik', 'Software Engineer', 56000))
repo.add_employee(Employee(102,'Abhishek', 'Software Automation Engineer', 40000))
repo.add_employee(Employee(103,'Rishabh', 'Software Automation Engineer', 99000))
repo.add_employee(Employee(104,'Nihar', 'Software Automation Engineer', 99))
repo.add_employee(Employee(105,'Divya', 'Business Analyst', 45000))

print(repo.employees)
emp_index = repo.search_employee(104)
if emp_index != -1:
    print('Searched employee:', repo.employees[emp_index])
else:
    print('Empoloyee Not Found.')

repo.update_employee(104,99200)
print(repo.employees)

repo.add_employee(Employee(106,'Mahesh', 'Python Trainer', 4200))
print(repo.employees)
repo.delete_employee(106)
print(repo.employees)
'''