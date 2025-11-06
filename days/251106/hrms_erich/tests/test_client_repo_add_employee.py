import pytest
import client.repo as repo
def test_add_employee_success():
    employee = {'name' : 'Gambhir',
        'job_title' : 'Coach',
        'salary' : 45000}
    created_employee = repo.add_employee(employee)

    queried_employee = repo.search_employee(created_employee['id'])

    #assertions
    assert queried_employee is not None 
    assert queried_employee['name'] == employee['name']

    
