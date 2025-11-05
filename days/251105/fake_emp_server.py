from flask import Flask, request, jsonify 

application = Flask(__name__)

employees = [
    {'id' : 101, 'name' : 'Abhishek'},
    {'id' : 102, 'name' : 'Dravid'}
]

@application.route('/employees', methods = ['GET'])
def read_all_employee():
    return jsonify(employees)

@application.route('/employees/<emp_id>', methods = ['GET'])
def read_employee_by_id(emp_id):
    emp_id = int(emp_id)
    queried_employee = None #
    for employee in employees:
        if employee['id'] == emp_id:
            queried_employee = employee
            break
    if not queried_employee: #
        return jsonify({'error' : 'Employee Not Found.'}), 404  #
    return jsonify(queried_employee)

application.run(debug = True)
