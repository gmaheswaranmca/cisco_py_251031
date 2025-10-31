def greet(name):
    result = f'Hello {name}'
    return result 

def hi(name):
    result = f'Hi {name}'
    return result 

person = input('Name:')
 
print(f'Hello {person}')

print(greet(person))
print(hi(person))