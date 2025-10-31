salaries = [] # list()

salaries.append(33000)
salaries.append(40000)
salaries.append(99000)

print(salaries)

#to remove the last salary 
#salaries.pop()

#to remove the salary based on index 
#salaries.pop(1)

#to remove the salary (figugre)
#salaries.remove(40000)

search = 40000
I = 0
search_index = -1 
for salary in salaries:
    if salary == search:
        search_index = I
        break 
    I += 1

print(search_index)





