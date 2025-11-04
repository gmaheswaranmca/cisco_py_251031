'''
    binary file persistence storage 
    using std module pickle
'''
import pickle
import os

FILE_NAME = 'employees_db.dat'
def read_employees():
    '''
        reads employees from db 
    '''
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, 'rb') as input_file:
        return pickle.load(input_file)

def write_employees(employees):
    '''
        writes employees into db
    '''
    with open(FILE_NAME, 'wb') as output_file:
        pickle.dump(employees, output_file)
