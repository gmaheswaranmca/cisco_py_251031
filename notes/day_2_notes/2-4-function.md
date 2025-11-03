## Creating User-Defined Functions in Python

User-defined functions allow you to organize your code into reusable blocks. Functions are defined using the `def` keyword, followed by the function name and parentheses containing any parameters.

### Syntax

```python
def function_name(parameters):
    """Optional docstring describing the function."""
    # Function body
    return value  # Optional
```

### Example: Basic Function

```python
def greet():
    print("Hello, world!")
```

Call the function:

```python
greet()  # Output: Hello, world!
```

### Example: Function with Parameters

```python
def add(a, b):
    return a + b
```

Call the function with arguments:

```python
result = add(3, 5)  # result is 8
```

### Return Statement

- The `return` statement sends a value back to the caller.
- If no `return` is specified, the function returns `None`.

### Docstrings

- Use triple quotes to document your function.
- Example:

```python
def square(x):
    """Returns the square of a number."""
    return x * x
```

### Why Use Functions?

- Code reuse
- Improved readability
- Easier maintenance

### Best Practices

- Use descriptive function names.
- Document functions with docstrings.
- Keep functions focused on a single task.

```
```

### Passing Functions as Arguments

In Python, functions are first-class objects. This means you can pass functions as arguments to other functions, return them from functions, and assign them to variables.

#### Example: Passing a Function to Another Function

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("Hello, World!")
    print(greeting)

greet(shout)   # Output: HELLO, WORLD!
greet(whisper) # Output: hello, world!
```

#### Use Cases

- **Callbacks:** Functions passed as arguments to be called later.
- **Customization:** Allow users to specify behavior by passing their own functions.
- **Functional Programming:** Use functions like `map`, `filter`, and `reduce` that accept other functions.

#### Example: Using Built-in Functions

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))  # [1, 4, 9, 16]
```

#### Key Points

- Functions can be passed just like variables.
- Useful for higher-order functions and functional programming patterns.
- Enables flexible and reusable code.

```
```

### Formal Arguments

Formal arguments are the variables listed in a function's definition. They act as placeholders for the values (actual arguments) that are passed when the function is called.

#### Example: Using Formal Arguments

```python
def multiply(x, y):
    return x * y
```

Here, `x` and `y` are formal arguments. When you call `multiply(2, 3)`, `2` and `3` are actual arguments.

#### Types of Formal Arguments

- **Positional Arguments:** Matched by position in the function call.
- **Keyword Arguments:** Matched by name, allowing arguments to be passed in any order.

##### Example: Keyword Arguments

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Alice")
```

#### Default Values

You can assign default values to formal arguments. If an argument is not provided, the default is used.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Sam")    # Output: Hello, Sam!
```

#### Key Points

- The number and order of formal arguments must match the function call unless using keyword arguments or defaults.
- Default arguments must follow non-default arguments in the function definition.
- Formal arguments make functions flexible and reusable.

```
```

### Variable-Length Arguments

Python allows you to define functions that accept a variable number of arguments using `*args` for positional arguments and `**kwargs` for keyword arguments.

#### Using `*args` (Non-Keyword Variable Arguments)

- Collects extra positional arguments as a tuple.

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))      # Output: 6
print(sum_all(4, 5, 6, 7))   # Output: 22
```

#### Using `**kwargs` (Keyword Variable Arguments)

- Collects extra keyword arguments as a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
# Output:
# name: Alice
# age: 25
```

#### Combining `*args` and `**kwargs`

You can use both in the same function, but `*args` must come before `**kwargs`.

```python
def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, a=3, b=4)
# Output:
# args: (1, 2)
# kwargs: {'a': 3, 'b': 4}
```

#### Key Points

- Use `*args` when you want to handle an arbitrary number of positional arguments.
- Use `**kwargs` for arbitrary keyword arguments.
- Useful for flexible APIs and wrapper functions.
- Default arguments and variable-length arguments can be combined, but order matters: regular arguments, then `*args`, then default arguments, then `**kwargs`.


```
```

### Walk-through of Built-in Functions

Python provides a rich set of built-in functions that are always available without needing to import any modules. These functions help perform common tasks efficiently.

#### Common Built-in Functions

- `len()`: Returns the length of an object (like a list, string, or dictionary).
    ```python
    fruits = ["apple", "banana", "cherry"]
    print(len(fruits))  # Output: 3
    ```

- `type()`: Returns the type of an object.
    ```python
    print(type(42))         # Output: <class 'int'>
    print(type("hello"))    # Output: <class 'str'>
    ```

- `max()` and `min()`: Return the largest and smallest items in an iterable.
    ```python
    numbers = [10, 20, 5, 8]
    print(max(numbers))  # Output: 20
    print(min(numbers))  # Output: 5
    ```

- `sum()`: Returns the sum of all items in an iterable.
    ```python
    print(sum([1, 2, 3, 4]))  # Output: 10
    ```

- `sorted()`: Returns a new sorted list from the items in an iterable.
    ```python
    names = ["Sam", "Alice", "Bob"]
    print(sorted(names))  # Output: ['Alice', 'Bob', 'Sam']
    ```

- `enumerate()`: Adds a counter to an iterable and returns it as an enumerate object.
    ```python
    for index, value in enumerate(["a", "b", "c"]):
        print(index, value)
    # Output:
    # 0 a
    # 1 b
    # 2 c
    ```

- `zip()`: Combines multiple iterables into tuples.
    ```python
    names = ["Alice", "Bob"]
    scores = [85, 90]
    for name, score in zip(names, scores):
        print(name, score)
    # Output:
    # Alice 85
    # Bob 90
    ```

#### Function-Related Built-ins

- `map()`: Applies a function to every item in an iterable.
    ```python
    def square(x):
        return x * x

    numbers = [1, 2, 3]
    print(list(map(square, numbers)))  # Output: [1, 4, 9]
    ```

- `filter()`: Filters items in an iterable using a function that returns `True` or `False`.
    ```python
    def is_even(x):
        return x % 2 == 0

    numbers = [1, 2, 3, 4]
    print(list(filter(is_even, numbers)))  # Output: [2, 4]
    ```

- `reduce()`: Applies a function cumulatively to the items of an iterable (from `functools` module).
    ```python
    from functools import reduce

    def multiply(x, y):
        return x * y

    numbers = [1, 2, 3, 4]
    print(reduce(multiply, numbers))  # Output: 24
    ```

#### Key Points

- Built-in functions simplify common programming tasks.
- Many built-ins work with iterables and support functional programming patterns.
- You can combine built-in functions for powerful data processing.

For a full list, see the [Python documentation on built-in functions](https://docs.python.org/3/library/functions.html).

```
```

## Functions in Python: Cheatsheet

- **Defining Functions:**  
    Use `def` keyword, function name, parameters in parentheses, and an optional docstring.
    ```python
    def my_func(param1, param2):
            """Docstring"""
            return param1 + param2
    ```

- **Calling Functions:**  
    Use function name with arguments.
    ```python
    my_func(1, 2)
    ```

- **Return Statement:**  
    Use `return` to send a value back. If omitted, returns `None`.

- **Docstrings:**  
    Document functions with triple quotes.

- **Function Arguments:**  
    - **Positional:** Matched by position.
    - **Keyword:** Matched by name.
    - **Default:** Assign default values.
    - **Variable-Length:**  
        - `*args` for extra positional arguments (tuple).
        - `**kwargs` for extra keyword arguments (dict).

- **Passing Functions:**  
    Functions are first-class objects; pass them as arguments, return them, assign to variables.
    ```python
    def greet(func): print(func("Hi"))
    greet(str.upper)
    ```

- **Built-in Functions:**  
    - `len()`, `type()`, `max()`, `min()`, `sum()`, `sorted()`, `enumerate()`, `zip()`
    - Functional: `map()`, `filter()`, `reduce()` (from `functools`)

- **Best Practices:**  
    - Use descriptive names.
    - Keep functions focused.
    - Document with docstrings.

- **Use Cases:**  
    - Code reuse
    - Readability
    - Callbacks
    - Flexible APIs

Refer to [Python built-in functions](https://docs.python.org/3/library/functions.html) for more.