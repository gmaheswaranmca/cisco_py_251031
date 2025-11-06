class EmployeeException(Exception):
    pass 

class EmployeeNotFoundError(EmployeeException):
    pass 

class EmployeeAlreadyExistError(EmployeeException):
    pass 

class DatabaseError(EmployeeException):
    pass 