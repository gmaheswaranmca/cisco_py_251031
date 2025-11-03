'''
Defines find_sum
Uses find_sum
'''
def find_sum_of_four(first, second, third, fourth, offset = 5, another_arg = 2):
    '''
    find_sum takes arguments and returns sum of the four numbers
    '''
    add_result = first + second + third + fourth + offset + another_arg
    multiply_result = first * second * third * fourth * offset * another_arg
    return add_result, multiply_result

print(find_sum_of_four(10, 20, 30, 40))
print(find_sum_of_four(third = 30, first = 10, fourth = 40, second = 20))
print(find_sum_of_four(10, 20, 30, 40, 6))
print(find_sum_of_four(10, 20, 30, 40, 6, 4))
print(find_sum_of_four(offset=3, third = 30, first = 10, fourth = 40, second = 20))
print(find_sum_of_four(offset=3, third = 30, first = 10, fourth = 40, second = 20, another_arg=17))
print('End of program')

def find_sum(first, second, *others):
    '''
    find_sum takes arguments and returns sum of the two or many positiona arguments numbers
    '''
    add_result = first + second
    for num in others:
        add_result += num

    print(type(first), type(second), type(others), others)
    return add_result

print(find_sum(1, 2, 3, 4, 5))

def find_sum_ka(first, second, **others):
    '''
    find_sum takes arguments and returns sum of the two or many numbers in keywords args 
    '''
    add_result = first + second
    for keyword in others:
        add_result += others[keyword]

    print(type(first), type(second), type(others), others)
    return add_result

print(find_sum_ka(first=1, second=2, third=3, fourth=4, fifth=5))
