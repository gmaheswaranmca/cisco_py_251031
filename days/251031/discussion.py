heap:
    ref1 : 'Dravid'  2 -> 1 -> 0
    ref2 : 'Hello Dravid' 0
    ref3 : 'Hello Dravid' 0
    ref4 : 'Hi Dravid' 1->0


stack:
    __main__    XXX
        person : ref1 XXX
    greet                   XXX
        name : ref1     XXX
        result : ref3  XXX  
    hi:                 XXX
        name : ref1 XXX
        result : ref4 XXX


================

Microsoft Windows [Version 10.0.21996.1]
(c) Microsoft Corporation. All rights reserved.

C:\mywork\source\workspaces\vpay>code .

C:\mywork\source\workspaces\vpay>python --version
Python 3.12.1

C:\mywork\source\workspaces\vpay>pip --version
pip 23.3.2 from C:\Users\gmahe\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)

C:\mywork\source\workspaces\vpay>git --version
git version 2.43.0.windows.1

C:\mywork\source\workspaces\vpay>python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print(10)
10
>>> print(10.5)
10.5
>>> print('Mahesh')
Mahesh
>>> print(2 > 3)
False
>>> 2 + 3
5
>>> 5 / 3
1.6666666666666667
>>> 5 // 3
1
>>> 10 // 3
3
>>> 10 % 3
1
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 3 ** 4
81
>>> 3 < 4
True
>>> 3 > 4
False
>>> 3 <= 4
True
>>> 3 >= 4
False
>>> 3 == 4
False
>>> 3 != 4
True
>>> mahesh = 46
>>> rishabh = 22
>>> abhi = 22
>>> (mahesh > rishabh) and (mahesh > abhi)
True
>>> (mahesh < rishabh) or (mahesh < abhi)
False
>>> (mahesh > rishabh) or (mahesh > abhi)
True
>>> (mahesh < rishabh) and (mahesh < abhi)
False
>>> type(5)
<class 'int'>
>>> type(5.2)
<class 'float'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(True)
<class 'bool'>
>>> type('mahesh')
<class 'str'>
>>> type([10,20,30])
<class 'list'>
>>> ages = [22, 33, 42, 21, 43, 18, 56, 22, 44]
>>> ages
[22, 33, 42, 21, 43, 18, 56, 22, 44]
>>> type(ages)
<class 'list'>
>>> ages = (22, 33, 42, 21, 43, 18, 56, 22, 44)
>>> ages
(22, 33, 42, 21, 43, 18, 56, 22, 44)
>>> type(ages)
<class 'tuple'>
>>> ages = {22, 33, 42, 21, 43, 18, 56, 22, 44}
>>> ages
{33, 42, 43, 44, 18, 21, 22, 56}
>>> type(ages)
<class 'set'>
>>> ages = [22, 33, 42, 21, 43, 18, 56, 22, 44]
>>> tuple(ages)
(22, 33, 42, 21, 43, 18, 56, 22, 44)
>>> set(ages)
{33, 42, 43, 44, 18, 21, 22, 56}
>>> list('Mahesh')
['M', 'a', 'h', 'e', 's', 'h']
>>> ages_freq = {22:2, 33:1, 42:1}
>>> type(ages_freq)
<class 'dict'>
>>> for I in range(len(ages)):
...     print(ages[I])
...
22
33
42
21
43
18
56
22
44
>>> for I in range(len(ages)):
...     print(f'Hi {ages[I]}')
...
Hi 22
Hi 33
Hi 42
Hi 21
Hi 43
Hi 18
Hi 56
Hi 22
Hi 44
>>> I = 0
>>> while I < len(ages):
...     print(f'Hi {ages[I]}')
...     I += 1
...
Hi 22
Hi 33
Hi 42
Hi 21
Hi 43
Hi 18
Hi 56
Hi 22
Hi 44
>>> for I in range(len(ages)):
...     age = ages[I]
...     if age <= 19:
...             print('Teen')
...     elif age <= 40:
...             print('Young')
...     elif age <= 60:
...             print('Middle')
...     elif age > 60:
...             print('Old')
...
Young
Young
Middle
Young
Middle
Teen
Middle
Young
Middle
>>> min_age = ages[0]
>>> for I in range(1,len(ages)):
...     age = ages[I]
...     if age < min_age:
...             min_age = age
... print(min_age)
  File "<stdin>", line 5
    print(min_age)
    ^^^^^
SyntaxError: invalid syntax
>>> min_age = ages[0]
>>> for I in range(len(ages)):
...
KeyboardInterrupt
>>> min_age = ages[0]
>>> min_age
22
>>> for I in range(1, len(ages)):
...     age = ages[I]
...     if age < min_age:
...             min_age = age
...
>>> print(min_age)
18
>>> sum(ages)
301
>>> sum(ages)/len(ages)
33.44444444444444
>>> avg(ages)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'avg' is not defined
>>> age_sum = 0
>>> for I in range(len(ages)):
...     age = ages[I]
...     age_sum += age
...
>>> age_sum
301
>>> age_sum / len(ages)
33.44444444444444
>>> dravid = {'name': 'Dravid', 'age':51}
>>> dravid
{'name': 'Dravid', 'age': 51}
>>> dravid = ('Dravid', 51)
>>> dravid
('Dravid', 51)
>>> dravid[1]
51
>>> class Employee:
...     def __init__(self, name, age):
...             self.name = name
...             self.age = age
...     def __repr__(self):
...             return f'[name = {self.name}, age = {self.age}]'
...     def __str__(self):
...             return self.__repr__()
...
>>> dravid = Employee('Dravid', 51)
>>> dravid
[name = Dravid, age = 51]
>>> dravid.age
51
>>> dravid = {'name': 'Dravid', 'age':51}
>>> dravid['age']
51
>>> 33000 * 88
2904000
>>> 29 * 12
348
>>>