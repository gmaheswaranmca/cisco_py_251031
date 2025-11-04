import pickle 

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

employees = [Employee(101,'Pratik', 'Software Engineer', 56000),
    Employee(102,'Abhishek', 'Software Automation Engineer', 40000),
    Employee(103,'Rishabh', 'Software Automation Engineer', 99000),
    Employee(104,'Nihar', 'Software Automation Engineer', 99),
    Employee(105,'Divya', 'Business Analyst', 45000)]

file_name = 'employees_db.dat'

print('To save employees into binary file...')
with open(file_name, 'wb') as out_file:
    pickle.dump(employees, out_file)
    print('Employees saved')

print('Access employees from binary file...')
with open(file_name, 'rb') as in_file:
    queried_employees = pickle.load(in_file)
    print('The queried employees from file:')
    print(queried_employees)

    

