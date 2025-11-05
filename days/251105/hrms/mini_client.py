import requests 

BASE_URL = 'http://127.0.0.1:5000'

# read all employees
url = f'{BASE_URL}/employees'
response = requests.get(url)
employees = response.json()
print(f'Employees List:\n{employees}')

#creaate employee
creatable_emp = {'name' : 'Dravid', 'job_title' : 'Old Coach', 'salary' : 1200}
url = f'{BASE_URL}/employees'
response = requests.post(url, json = creatable_emp)
created_emp = response.json()
print(f'Created Employee:{created_emp}')

# read all employees
url = f'{BASE_URL}/employees'
response = requests.get(url)
employees = response.json()
print(f'Employees List:\n{employees}')

# read employee by id
url = f'{BASE_URL}/employees/{created_emp["id"]}'
response = requests.get(url)
employee = response.json()
print(f'Read by id:\n{employee}')

# update employee 
url = f'{BASE_URL}/employees/{created_emp["id"]}'
body = {'salary' : 1201}
response = requests.put(url, json = body)
employee = response.json()
print(f'Updated employee\n{employee}')

# delete employee 
url = f'{BASE_URL}/employees/{created_emp["id"]}'
response = requests.delete(url)
message = response.json()
print(f'Employee Deleted message\n{message}')