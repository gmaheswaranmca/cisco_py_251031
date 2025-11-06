'''
    api repo
'''
import requests 

BASE_URL = 'http://127.0.0.1:5000'

def read_all_employees():
    url = f'{BASE_URL}/employees'
    response = requests.get(url)
    employees = response.json()
    return employees 

def add_employee(employee):
    url = f'{BASE_URL}/employees'
    response = requests.post(url, json = employee)
    created_emp = response.json()
    return created_emp

def search_employee(id): 
    url = f'{BASE_URL}/employees/{id}'
    response = requests.get(url)
    employee = response.json()

    if response.status_code != 200:
        return None 
    return employee
 
def update_employee(id, salary):
    url = f'{BASE_URL}/employees/{id}'
    body = {'salary' : salary}
    response = requests.put(url, json = body)
    if response.status_code != 200:
        return None 
    employee = response.json()
    return employee     
  
def delete_employee(id):
    url = f'{BASE_URL}/employees/{id}'
    response = requests.delete(url)
    if response.status_code != 200:
        return None 
    message = response.json()
    return message