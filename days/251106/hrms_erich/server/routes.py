from flask import Flask, request, jsonify 

import server.repo as repo 
from mailer.mail import send_gmail, to_address

application = Flask(__name__)

# configure the db 
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp_app_db.sqlite'
application.config['SQLALCHEMY_ECHO'] = True 
repo.db.init_app(application)
#       create tables
with application.app_context():
    repo.db.create_all()
# end configure the db 


@application.route('/employees', methods = ['GET'])
def read_all_employee():
    employees = repo.read_all_employees()
    employees_dict = [employee.to_dict() for employee in employees]
    return jsonify(employees_dict)

@application.route('/employees/<emp_id>', methods = ['GET'])
def read_employee_by_id(emp_id):
    emp_id = int(emp_id)
    queried_employee = repo.search_employee(emp_id)
    if not queried_employee: #
        return jsonify({'error' : 'Employee Not Found.'}), 404  #
    return jsonify(queried_employee.to_dict())

@application.route('/employees', methods = ['POST'])
def create_employee():
    form_employee = request.json
    employee = repo.Employee(name = form_employee['name'],
            job_title = form_employee['job_title'],
            salary = form_employee['salary'])
    
    try:
        repo.add_employee(employee)
        created_employee = repo.search_employee(employee.id)
    except repo.EmployeeAlreadyExistError as ex:
        return jsonify({'error' : 'Server Error'}), 500
    except repo.DatabaseError as ex:
        return jsonify({'error' : 'Server Error'}), 500

    #sending creation mail
    subject = f'{created_employee.name} is created'
    body = f'''ID : {created_employee.id}
Name: {created_employee.name}
Job Title: {created_employee.job_title}
Salary : ${created_employee.salary}
'''
    send_gmail(to_address = to_address, 
               subject = subject, 
               body = body)
    # log the mail sent info 
    #end sending creation mail
    return jsonify(created_employee.to_dict()), 201

@application.route('/employees/<emp_id>', methods = ['PUT'])
def update_employee(emp_id):
    emp_id = int(emp_id)
    queried_employee = repo.search_employee(emp_id)
    if not queried_employee: #
        return jsonify({'error' : 'Employee Not Found.'}), 404  #
    
    form_employee = request.json
    repo.update_employee(emp_id, form_employee['salary'])

    updated_employee = repo.search_employee(emp_id)
    return jsonify(updated_employee.to_dict())

@application.route('/employees/<emp_id>', methods = ['DELETE'])
def delete_employee(emp_id):
    emp_id = int(emp_id)
    queried_employee = repo.search_employee(emp_id)
    if not queried_employee: #
        return jsonify({'error' : 'Employee Not Found.'}), 404  # 
    
    repo.delete_employee(emp_id)
    return jsonify({'message' : 'Employee Deleted Successfully'})

#application.run(debug = True)