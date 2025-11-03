## Numbers and Expressions in Python

Python supports several numeric types and provides a rich set of operators for working with numbers.

### Numeric Types

- **Integers (`int`)**: Whole numbers, e.g., `5`, `-42`, `1000000`
- **Floating-point numbers (`float`)**: Numbers with decimals, e.g., `3.14`, `-0.001`, `2.0`
- **Complex numbers (`complex`)**: Numbers with real and imaginary parts, e.g., `2 + 3j`

### Basic Arithmetic Operators

| Operator | Description        | Example      | Result   |
|----------|-------------------|--------------|----------|
| `+`      | Addition          | `2 + 3`      | `5`      |
| `-`      | Subtraction       | `5 - 2`      | `3`      |
| `*`      | Multiplication    | `4 * 3`      | `12`     |
| `/`      | Division          | `7 / 2`      | `3.5`    |
| `//`     | Floor Division    | `7 // 2`     | `3`      |
| `%`      | Modulus (remainder)| `7 % 2`     | `1`      |
| `**`     | Exponentiation    | `2 ** 3`     | `8`      |

### Expressions

- Expressions combine values and operators to produce new values.
- Python follows standard mathematical precedence (PEMDAS/BODMAS).
- Parentheses `()` can be used to group expressions and control evaluation order.

```python
result = (2 + 3) * 4  # result is 20
```

### Type Conversion

- Use `int()`, `float()`, and `complex()` to convert between numeric types.
- Automatic type conversion occurs in mixed-type expressions (e.g., `2 + 3.0` yields `5.0`).

### Useful Built-in Functions

- `abs(x)`: Absolute value
- `round(x, n)`: Round to `n` decimal places
- `pow(x, y)`: Power, equivalent to `x ** y`
- `divmod(a, b)`: Returns tuple `(a // b, a % b)`

### Mathematical Module

- The `math` module provides advanced mathematical functions:
    ```python
    import math
    print(math.sqrt(16))  # 4.0
    print(math.sin(math.pi / 2))  # 1.0
    ```

### Best Practices

- Use descriptive variable names for numeric values.
- Avoid floating-point equality checks due to precision issues; use `math.isclose()` if needed.

### Example

```python
a = 10
b = 3
print(a + b)      # 13
print(a / b)      # 3.333...
print(a // b)     # 3
print(a % b)      # 1
print(a ** b)     # 1000
```

```
```

## Variables and Statements in Python

Variables are used to store data values in Python. Statements are instructions that the Python interpreter executes.

### Variables

- **Definition**: A variable is a name that refers to a value stored in memory.
- **Assignment**: Use the `=` operator to assign a value to a variable.
    ```python
    x = 5
    name = "Alice"
    pi = 3.14159
    ```
- **Naming Rules**:
    - Must start with a letter or underscore (`_`)
    - Can contain letters, digits, and underscores
    - Case-sensitive (`myVar` and `myvar` are different)
    - Avoid using Python keywords (e.g., `for`, `if`, `class`)
- **Multiple Assignment**:
    ```python
    a, b, c = 1, 2, 3
    x = y = 0  # Both x and y are 0
    ```
- **Swapping Values**:
    ```python
    a, b = b, a
    ```

### Statements

- **Expression Statement**: Evaluates an expression.
    ```python
    print(x + 2)
    ```
- **Assignment Statement**: Assigns a value to a variable.
    ```python
    total = a + b
    ```
- **Compound Statements**: Consist of multiple lines, such as loops and conditionals.

### Updating Variables

- Variables can be updated using assignment and arithmetic operators.
    ```python
    count = 0
    count = count + 1  # Increment
    count += 1         # Shorthand for increment
    ```

### Dynamic Typing

- Python variables are dynamically typed; their type can change during execution.
    ```python
    x = 10      # x is an int
    x = "ten"   # x is now a str
    ```

### Deleting Variables

- Use `del` to remove a variable from memory.
    ```python
    del x
    ```

### Best Practices

- Use descriptive names that reflect the variable's purpose.
- Use lowercase with underscores for variable names (`snake_case`).
- Avoid overwriting built-in names (e.g., `list`, `str`).

### Example

```python
age = 25
name = "Bob"
height = 1.75

print(name, "is", age, "years old and", height, "meters tall.")
```

```
```

## Conditional Statements and Loops in Python

Conditional statements and loops are fundamental for controlling the flow of a Python program.

### Conditional Statements

- **`if` Statement**: Executes code if a condition is true.
    ```python
    if x > 0:
        print("x is positive")
    ```
- **`if-else` Statement**: Provides an alternative if the condition is false.
    ```python
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
    ```
- **`elif` (Else If)**: Checks multiple conditions in sequence.
    ```python
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    ```
- **Nested Conditionals**: Conditionals can be nested for complex logic.
    ```python
    if x > 0:
        if x < 10:
            print("x is between 1 and 9")
    ```

### Comparison and Logical Operators

- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `and`, `or`, `not`
    ```python
    if age > 18 and age < 65:
        print("Adult")
    ```

### Loops

#### `while` Loop

- Repeats as long as a condition is true.
    ```python
    count = 0
    while count < 5:
        print(count)
        count += 1
    ```

#### `for` Loop

- Iterates over a sequence (list, tuple, string, range, etc.).
    ```python
    for i in range(5):
        print(i)
    ```
- Can iterate over any iterable object.
    ```python
    for char in "Python":
        print(char)
    ```

#### Loop Control Statements

- **`break`**: Exit the loop immediately.
    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```
- **`continue`**: Skip the rest of the current iteration.
    ```python
    for i in range(5):
        if i == 2:
            continue
        print(i)
    ```
- **`else`**: Optional block executed if the loop completes normally (not via `break`).
    ```python
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            print(n, "is prime")
    ```

### Best Practices

- Use indentation (4 spaces) to define code blocks.
- Keep conditions clear and concise.
- Avoid infinite loops by ensuring loop conditions will eventually be false.

### Example

```python
number = int(input("Enter a number: "))
if number < 0:
    print("Negative number")
elif number == 0:
    print("Zero")
else:
    print("Positive number")

for i in range(1, 6):
    print("Iteration", i)
```

```
```

## Handling User Input in Python

Handling user input allows your program to interact with users and respond to their actions.

### Reading Input

- Use the `input()` function to read a line of text from the user.
    ```python
    name = input("Enter your name: ")
    print("Hello,", name)
    ```
- The input is always returned as a string.

### Converting Input Types

- Convert input to other types as needed:
    ```python
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    ```
- Use `int()`, `float()`, or `str()` for conversion.

### Handling Invalid Input

- Use `try` and `except` blocks to handle conversion errors:
    ```python
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    ```

### Input with Multiple Values

- Split input into multiple values using `split()`:
    ```python
    x, y = input("Enter two numbers separated by space: ").split()
    x = int(x)
    y = int(y)
    ```

### Example

```python
username = input("What is your username? ")
age = int(input("How old are you? "))
print(f"Welcome, {username}! You are {age} years old.")
```

### Best Practices

- Always validate and sanitize user input.
- Provide clear prompts to guide the user.
- Handle exceptions to prevent program crashes.


```
```

## Overview of Built-in Functions and Modules in Python

Python provides a wide range of built-in functions and modules to simplify programming tasks.

### Built-in Functions

- **Common Built-ins**:
    - `print()`: Output to the console.
    - `len()`: Get the length of a sequence.
    - `type()`: Get the type of an object.
    - `input()`: Read user input.
    - `max()`, `min()`: Find maximum or minimum value.
    - `sum()`: Sum elements of an iterable.
    - `sorted()`: Return a sorted list.
    - `range()`: Generate a sequence of numbers.
    - `enumerate()`: Iterate with index and value.
    - `zip()`: Combine multiple iterables.
    - `map()`, `filter()`: Functional programming utilities.
    - `isinstance()`: Check object type.

- **Examples**:
    ```python
    numbers = [1, 2, 3]
    print(len(numbers))           # 3
    print(sum(numbers))           # 6
    print(sorted(numbers))        # [1, 2, 3]
    print(type(numbers))          # <class 'list'>
    ```

### Built-in Modules

- **Importing Modules**:
    - Use `import` to access modules.
    - Example: `import math`, `import random`

- **Common Modules**:
    - `math`: Mathematical functions (`math.sqrt()`, `math.pi`)
    - `random`: Random number generation (`random.randint()`)
    - `datetime`: Date and time manipulation
    - `os`: Operating system interfaces
    - `sys`: System-specific parameters and functions
    - `json`: JSON encoding and decoding
    - `re`: Regular expressions

- **Example Usage**:
    ```python
    import random
    print(random.randint(1, 10))  # Random integer between 1 and 10

    import datetime
    print(datetime.datetime.now())  # Current date and time
    ```

### Finding More Built-ins and Modules

- Use `dir(__builtins__)` to list all built-in functions.
- The [Python Standard Library documentation](https://docs.python.org/3/library/) lists all available modules.

### Best Practices

- Prefer built-in functions and modules for common tasks—they are efficient and well-tested.
- Use `help()` to get documentation for functions and modules.
- Avoid redefining built-in names in your code.

```
```

## Python Syntax, Style, and Coding Conventions

Understanding Python's syntax and following style conventions helps write readable, maintainable code.

### Python Syntax Basics

- **Indentation**: Python uses indentation (typically 4 spaces) to define code blocks.
    ```python
    if x > 0:
        print("Positive")
    ```
- **Statements End**: No need for semicolons; each statement ends at the line break.
- **Comments**: Use `#` for single-line comments.
    ```python
    # This is a comment
    ```
- **Docstrings**: Use triple quotes for documentation within functions/classes.
    ```python
    def func():
        """This function does something."""
        pass
    ```
- **Line Continuation**: Use `\` or parentheses for long lines.
    ```python
    total = (a +
             b +
             c)
    ```

### Naming Conventions

- **Variables/Functions**: Use `snake_case` (lowercase with underscores).
    ```python
    user_name = "Alice"
    def calculate_total():
        pass
    ```
- **Classes**: Use `CamelCase`.
    ```python
    class MyClass:
        pass
    ```
- **Constants**: Use `UPPERCASE`.
    ```python
    PI = 3.14159
    ```

### PEP 8 – Style Guide for Python Code

- **Indentation**: 4 spaces per level.
- **Maximum Line Length**: 79 characters.
- **Blank Lines**: Use blank lines to separate functions/classes.
- **Imports**: Place imports at the top, one per line.
    ```python
    import os
    import sys
    ```
- **Whitespace**: Avoid extra spaces inside parentheses, brackets, or before commas.
    ```python
    print(a, b)
    ```

### Other Conventions

- **Function/Variable Naming**: Be descriptive and concise.
- **Avoid Global Variables**: Prefer local variables and function arguments.
- **Error Handling**: Use exceptions (`try`, `except`) for error management.
- **Readability**: Write code for humans first, computers second.

### Example

```python
def get_user_age():
    """Prompt user for age and return as integer."""
    age = int(input("Enter your age: "))
    return age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = Person("Alice", get_user_age())
print(f"{user.name} is {user.age} years old.")
```

### Resources

- [PEP 8 – Python Style Guide](https://peps.python.org/pep-0008/)
- Use `flake8` or `pylint` for automated style checks.

```
```

## Basic Introspection in Python (`type()`, `dir()`)

Introspection allows you to examine objects, types, and capabilities at runtime, which is useful for debugging and exploration.

### `type()` Function

- Returns the type of an object.
    ```python
    print(type(42))         # <class 'int'>
    print(type("hello"))    # <class 'str'>
    print(type([1, 2, 3]))  # <class 'list'>
    ```
- Useful for checking or validating data types.

### `dir()` Function

- Lists the attributes and methods of an object.
    ```python
    print(dir("hello"))
    # Shows string methods like 'upper', 'lower', etc.
    print(dir(list))
    # Shows list methods like 'append', 'extend', etc.
    ```
- Helps discover available operations and properties.

### Other Introspection Tools

- `help(obj)`: Displays documentation for an object.
    ```python
    help(str)
    help(list.append)
    ```
- `isinstance(obj, type)`: Checks if an object is an instance of a type.
    ```python
    if isinstance(x, int):
        print("x is an integer")
    ```

### Example

```python
value = [1, 2, 3]
print(type(value))      # <class 'list'>
print(dir(value))       # List all list methods
help(value.append)      # Documentation for append method
```

### Best Practices

- Use introspection to explore unfamiliar objects or modules.
- Combine `type()`, `dir()`, and `help()` for effective debugging and learning.
- Avoid relying on introspection for production logic; use it mainly for development and troubleshooting.

```
```

## Python Quick Reference Cheatsheet

### Numbers and Expressions
- Numeric types: `int`, `float`, `complex`
- Operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Type conversion: `int()`, `float()`, `complex()`
- Useful functions: `abs()`, `round()`, `pow()`, `divmod()`
- Math module: `import math`

### Variables and Statements
- Assignment: `x = 5`
- Naming: letters, digits, underscores; case-sensitive
- Multiple assignment: `a, b = 1, 2`
- Update: `x += 1`
- Dynamic typing: variable types can change
- Delete: `del x`

### Conditional Statements and Loops
- `if`, `elif`, `else` for branching
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `and`, `or`, `not`
- Loops: `while`, `for`
- Loop control: `break`, `continue`, `else` on loops

### Handling User Input
- Input: `input("Prompt")` (returns string)
- Convert: `int()`, `float()`
- Error handling: `try`/`except`
- Multiple values: `input().split()`

### Built-in Functions and Modules
- Common functions: `print()`, `len()`, `type()`, `max()`, `min()`, `sum()`, `sorted()`, `range()`, `enumerate()`, `zip()`, `map()`, `filter()`, `isinstance()`
- Import modules: `import math`, `import random`
- Standard library: `os`, `sys`, `datetime`, `json`, `re`

### Python Syntax, Style, and Coding Conventions
- Indentation: 4 spaces
- Comments: `#`
- Docstrings: triple quotes
- Naming: `snake_case` for variables/functions, `CamelCase` for classes, `UPPERCASE` for constants
- Follow [PEP 8](https://peps.python.org/pep-0008/)

### Basic Introspection
- `type(obj)`: get type
- `dir(obj)`: list attributes/methods
- `help(obj)`: documentation
- `isinstance(obj, type)`: type check


