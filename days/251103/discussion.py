1. multi module
    employee_model.py
    ->
    /app 
        - employee.py       Employee
        - repo.py           crud fns, employees 
        - run.py            imported employee and repo modules 

2. functions 
    takes args
    may returns result : one or more 

    args 
    - positional arg 
    - keyword arg 
    - default arg 
    - variable arg 
        - positional variable args :: tuple  
        - keyword variable args :: dict 

3. str, list, tuple, dict, set, file 
    ### Problem 1

    Write a Python program that:

    1. Accepts a sequence of words from the user in a single line (separated by spaces).
    2. Stores the words in both a **list** and a **tuple**.
    3. Displays the list and tuple on the screen.
    4. Saves the list and tuple into a text file named **`qn01_data.txt`**.
    5. Reads back the saved data from the file and prints it on the screen.

    ---

    ### Problem 2

    Write a Python program that:

    1. Reads a line of integers from the user (separated by spaces).
    2. Stores them in a **list** and calculates the **sum and average**.
    3. Saves the list, sum, and average into a text file named **`numbers_data.txt`**.
    4. Reads the contents of the file and prints them back to the user.

    ---

    ### Problem 3

    Write a Python program that:

    1. Accepts a sentence from the user.
    2. Splits the sentence into words and stores them in a **list**.
    3. Converts all words to **uppercase** and stores them in a **tuple**.
    4. Saves both the list and tuple into a file named **`sentence_data.txt`**.
    5. Reads back the data from the file and displays it on the screen.

    ---

    ### Problem 4

    Write a Python program that:

    1. Reads a list of names from the user (separated by spaces).
    2. Sorts the names alphabetically and stores them in a list.
    3. Converts the list into a tuple.
    4. Saves the sorted list and tuple into a file named **`names_data.txt`**.
    5. Reads and prints the saved data from the file.

    ---

    ### Problem 5

    Write a Python program that:

    1. Accepts a sequence of numbers from the user.
    2. Stores the numbers in a list and finds the **maximum and minimum values**.
    3. Stores the results (list, max, min) in a file named **`minmax_data.txt`**.
    4. Reads and prints the saved data from the file.


C: 
    101,Aaris,TCE,90000
    int,char[255],char[125],long
    4   255       125       8     = 392

392
392
392
392


101,Aaris,TCE,90000
[8,5,3,8]101AarisTCE90000

====

C:\mywork\source\workspaces\cisco_py_251031\days\251103>python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> u_str = 'hello'
>>> u_str
'hello'
>>> b_str = b'hello'
>>> b_str
b'hello'
>>> name = 'Maheswaran'
>>> name[0]
'M'
>>> name[2]
'h'
>>> name[-1]
'n'
>>> name[-2]
'a'
>>> name[::2]
'Mhsaa'
>>> name[0::1]
'Maheswaran'
>>> name[0:5:1]
'Mahes'
>>> name[0:5:2]
'Mhs'
>>> name[::-1]
'narawsehaM'
>>> name[-1::-1]
'narawsehaM'
>>> 'ran' in 'Maheswaran'
True
>>> 'run' in 'Maheswaran'
False
>>> len('Maheswaran')
10
>>> sorted('Maheswaran')
['M', 'a', 'a', 'a', 'e', 'h', 'n', 'r', 's', 'w']
>>> sorted('maheswaran')
['a', 'a', 'a', 'e', 'h', 'm', 'n', 'r', 's', 'w']
>>> asc('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'asc' is not defined
>>> ascii('a')
"'a'"
>>> ord('a')
97
>>> ord('A')
65
>>> ord('0')
48
>>> chr(65)
'A'
>>> chr(97)
'a'
>>> nums = (10, 20, 30)
>>> nums
(10, 20, 30)
>>> nums = (10, )
>>> nums = [10, 20, 30, ]
>>> nums
[10, 20, 30]
>>> nums_freq = {10:1, 20:2, 30:5, }
>>> nums_freq
{10: 1, 20: 2, 30: 5}
>>> nums = [10, 5, 6, 8, 3, 1]
>>> nums.extend((4, 7, 9))
>>> nums
[10, 5, 6, 8, 3, 1, 4, 7, 9]
>>> sorted(nums)
[1, 3, 4, 5, 6, 7, 8, 9, 10]
>>> nums
[10, 5, 6, 8, 3, 1, 4, 7, 9]
>>> nums.sort()
>>> nums
[1, 3, 4, 5, 6, 7, 8, 9, 10]
>>> nums = [10, 5, 6, 8, 3, 1]
>>> reversed(nums)
<list_reverseiterator object at 0x000002532519BEB0>
>>> list(reversed(nums))
[1, 3, 8, 6, 5, 10]
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(list.sort())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unbound method list.sort() needs an argument
>>> help(list.sort)
Help on method_descriptor:

sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.

    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).

    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.

    The reverse flag can be set to sort in descending order.

>>> a = 10
>>> b = 20
>>> b,a=a,b
>>> b
10
>>> a
20
>>> a,b=10,20
>>> t = (10,20,30,40)
>>> p,*others=t
>>> p
10
>>> others
[20, 30, 40]
>>> import pickle
>>> employees = [{'id':101,'name':'Aaris','job_title':'TCE','salary':90000}]
>>> with open('employees.dat','wb') as out_file:
...     pickle.dump(employees, out_file)
...
>>> with open('employees.dat','rb') as in_file:
...     file_employees = pickle.load(in_file)
...     print(file_employees)
...
[{'id': 101, 'name': 'Aaris', 'job_title': 'TCE', 'salary': 90000}]