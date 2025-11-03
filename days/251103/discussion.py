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
