## Standard Python Modules (Quick Overview)

### Python Decorators
Decorators are functions that modify the behavior of other functions or classes. They are commonly used for logging, access control, memoization, and more.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")
```

- `@decorator` syntax applies the decorator to the function.
- Built-in decorators: `@staticmethod`, `@classmethod`, `@property`.

### Generators
Generators are functions that yield values one at a time using the `yield` keyword. They are memory-efficient for large data sets.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
```

- Generator expressions: `(x*x for x in range(10))`
- Useful for streaming data, pipelines.

### `sys` and `os` Modules
- `sys`: Access system-specific parameters and functions.
  - `sys.argv`: Command-line arguments.
  - `sys.exit()`: Exit the program.
  - `sys.path`: Module search paths.
- `os`: Interact with the operating system.
  - `os.getcwd()`: Get current directory.
  - `os.listdir()`: List files in a directory.
  - `os.environ`: Environment variables.
  - `os.path`: Path manipulations.

### Object Persistence Modules
- `pickle`: Serialize and deserialize Python objects.
  ```python
  import pickle
  data = {'a': 1, 'b': 2}
  with open('data.pkl', 'wb') as f:
      pickle.dump(data, f)
  with open('data.pkl', 'rb') as f:
      loaded = pickle.load(f)
  ```
- `shelve`: Persistent, dictionary-like object storage.
  ```python
  import shelve
  with shelve.open('mydata') as db:
      db['key'] = [1, 2, 3]
  ```

### `time` and `datetime` Modules
- `time`: Basic time-related functions.
  - `time.time()`: Current timestamp.
  - `time.sleep(seconds)`: Pause execution.
- `datetime`: Manipulate dates and times.
  ```python
  from datetime import datetime, timedelta
  now = datetime.now()
  future = now + timedelta(days=5)
  print(now.strftime("%Y-%m-%d %H:%M:%S"))
  ```

### File-related Modules & Logging
- File I/O: `open()`, `read()`, `write()`, `with` statement for context management.
  ```python
  with open('file.txt', 'r') as f:
      content = f.read()
  ```
- `logging`: Flexible logging system.
  ```python
  import logging
  logging.basicConfig(level=logging.INFO)
  logging.info("This is an info message")
  ```

### `re`, `numpy`, and `pandas`
- `re`: Regular expressions for pattern matching.
  ```python
  import re
  match = re.search(r'\d+', 'abc123')
  ```
- `numpy`: Numerical computing, arrays, linear algebra.
  ```python
  import numpy as np
  arr = np.array([1, 2, 3])
  ```
- `pandas`: Data analysis, DataFrames, CSV/Excel I/O.
  ```python
  import pandas as pd
  df = pd.read_csv('data.csv')
  ```

---

## Python Decorators

Decorators wrap functions to extend their behavior without modifying their code.

### Function Decorators

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b
```

### Decorators with Arguments

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")
```

### Class Decorators

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MyClass:
    pass
```

### Built-in Decorators

- `@staticmethod`: Defines a static method.
- `@classmethod`: Defines a class method.
- `@property`: Defines a property.

### `functools.wraps`

Use `functools.wraps` to preserve metadata of the original function.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Decorators are powerful tools for code reuse and separation of concerns.

```
```


### Detailed Notes: Python Decorators

#### What Are Decorators?
Decorators are higher-order functions that take another function or class and extend or alter its behavior without explicitly modifying its code. They are widely used for cross-cutting concerns like logging, authentication, timing, caching, and more.

#### Syntax and Usage

- The `@decorator` syntax is syntactic sugar for `func = decorator(func)`.
- Decorators can be applied to functions, methods, and classes.

```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f"Hello, {name}!")
```

#### Function Decorators

- Used to wrap functions and modify their behavior.

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b
```

#### Decorators with Arguments

- Decorators can accept arguments by nesting functions.

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")
```

#### Class Decorators

- Decorators can be used to modify or enhance classes.

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    pass
```

#### Built-in Decorators

- `@staticmethod`: Defines a static method (no `self` or `cls`).
- `@classmethod`: Defines a class method (receives `cls` as first argument).
- `@property`: Defines a getter for a property.

```python
class Example:
    @staticmethod
    def foo():
        return "static"

    @classmethod
    def bar(cls):
        return "class"

    @property
    def baz(self):
        return "property"
```

#### Preserving Metadata with `functools.wraps`

- Use `functools.wraps` to preserve the original function’s name, docstring, and other metadata.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

#### Chaining Multiple Decorators

- Multiple decorators can be stacked; they are applied from the closest to the function outward.

```python
@decorator_one
@decorator_two
def my_func():
    pass
```

#### Practical Use Cases

- **Logging**: Track function calls and arguments.
- **Access Control**: Restrict access based on user roles.
- **Memoization**: Cache results for expensive computations.
- **Validation**: Check arguments before function execution.

#### Decorators for Classes

- Decorators can also be used to modify class behavior, such as enforcing singleton patterns or registering classes.

#### Summary

- Decorators are a powerful feature for code reuse and separation of concerns.
- They can be customized, parameterized, and combined for flexible functionality.
- Built-in decorators simplify common patterns in object-oriented programming.


```
```


### Detailed Notes: Generators

#### What Are Generators?
Generators are special functions that return an iterator object which yields values one at a time, using the `yield` keyword. Unlike regular functions, generators do not compute all values at once; they produce them on demand, making them memory-efficient for large datasets.

#### Syntax and Usage

- Define a generator function using `def` and `yield`.
- Calling the function returns a generator object, not the values directly.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(5)
for num in gen:
    print(num)
```

#### How Generators Work

- Each call to `yield` pauses the function and saves its state.
- Execution resumes from the last `yield` when the next value is requested.
- Generators raise `StopIteration` when exhausted.

#### Generator Expressions

- Similar to list comprehensions, but use parentheses and produce values lazily.

```python
squares = (x*x for x in range(10))
for sq in squares:
    print(sq)
```

#### Advantages of Generators

- **Memory Efficiency**: Only one item is in memory at a time.
- **Lazy Evaluation**: Values are computed as needed.
- **Infinite Sequences**: Can model streams or infinite data.

#### Common Use Cases

- Reading large files line by line.
- Processing data streams.
- Generating sequences (e.g., Fibonacci numbers).

#### Example: Infinite Generator

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

#### `next()` Function

- Use `next(generator)` to manually get the next value.
- Can provide a default value to avoid `StopIteration`.

```python
gen = (x for x in range(3))
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
```

#### Generator Methods

- `.send(value)`: Sends a value to the generator.
- `.throw(exception)`: Raises an exception inside the generator.
- `.close()`: Terminates the generator.

#### Comparison: Generators vs. Iterators

- All generators are iterators, but not all iterators are generators.
- Generators are defined with `yield`; iterators implement `__iter__` and `__next__`.

#### Summary

- Generators are ideal for handling large or infinite data streams.
- They enable efficient, readable, and maintainable code for iterative processes.
- Generator expressions offer concise syntax for simple generators.

### Custom Iterator Example

#### Creating a Custom Iterator Class

A custom iterator is a class that implements the `__iter__()` and `__next__()` methods. This allows you to define your own iteration logic.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Usage
for num in Countdown(5):
    print(num)
```

**Output:**
```
5
4
3
2
1
```

#### Key Points

- `__iter__()` returns the iterator object itself.
- `__next__()` returns the next value or raises `StopIteration` when done.
- Custom iterators are useful for complex iteration patterns not easily handled by generators.



```
```


### Detailed Notes: `sys` and `os` Modules

#### The `sys` Module

The `sys` module provides access to system-specific parameters and functions used or maintained by the Python interpreter.

**Common Features:**

- `sys.argv`: List of command-line arguments passed to the script.
    ```python
    import sys
    print(sys.argv)  # ['script.py', 'arg1', 'arg2']
    ```
- `sys.exit([status])`: Exits the program with an optional status code.
    ```python
    sys.exit(0)
    ```
- `sys.path`: List of directories Python searches for modules.
    ```python
    print(sys.path)
    ```
- `sys.version`: Python version info.
    ```python
    print(sys.version)
    ```
- `sys.stdin`, `sys.stdout`, `sys.stderr`: File objects for input/output/error streams.

**Use Cases:**
- Handling command-line arguments.
- Exiting scripts gracefully.
- Modifying module search paths.

#### The `os` Module

The `os` module provides a way to interact with the operating system, including file and directory operations, environment variables, and process management.

**Common Features:**

- `os.getcwd()`: Get current working directory.
    ```python
    import os
    print(os.getcwd())
    ```
- `os.listdir(path)`: List files and directories in a given path.
    ```python
    print(os.listdir('.'))
    ```
- `os.environ`: Access environment variables.
    ```python
    print(os.environ['PATH'])
    ```
- `os.path`: Utilities for file path manipulations.
    - `os.path.join()`, `os.path.exists()`, `os.path.abspath()`
    ```python
    print(os.path.join('folder', 'file.txt'))
    print(os.path.exists('file.txt'))
    ```
- `os.remove()`, `os.rename()`, `os.mkdir()`, `os.rmdir()`: File and directory operations.

**Process Management:**
- `os.system(command)`: Run a shell command.
    ```python
    os.system('echo Hello')
    ```
- `os.execvp()`, `os.fork()`, `os.getpid()`: Advanced process control (Unix only).

**Cross-Platform Considerations:**
- Use `os.path` for file paths to ensure compatibility across Windows, macOS, and Linux.

#### Summary

- `sys` is for Python interpreter and runtime environment control.
- `os` is for interacting with the operating system, files, directories, and environment variables.
- Both modules are essential for scripting, automation, and system-level programming in Python.

#### Advanced Features of the `os` Module

- **File Permissions and Metadata:**
    - `os.chmod(path, mode)`: Change file permissions.
    - `os.stat(path)`: Get file metadata (size, modification time, etc.).
    - `os.utime(path, times)`: Update file access and modification times.

- **Walking Directory Trees:**
    - `os.walk(top)`: Generate file names in a directory tree.
    ```python
    for root, dirs, files in os.walk('.'):
        print(root, dirs, files)
    ```

- **Temporary Files and Directories:**
    - Use the `tempfile` module (often with `os`) for creating temporary files/directories.

- **Platform Information:**
    - `os.name`: Indicates the operating system type (`'posix'`, `'nt'`, etc.).
    - `os.uname()`: System information (Unix only).

- **Environment Manipulation:**
    - `os.putenv(key, value)`: Set environment variable (not always recommended; use `os.environ`).

- **Path Manipulation Utilities:**
    - `os.path.split()`, `os.path.basename()`, `os.path.dirname()`: Split and extract parts of file paths.

#### Best Practices

- Prefer `os.path` and `os` functions over hardcoded paths and shell commands for portability.
- Use exception handling (`try...except`) for file and directory operations to handle errors gracefully.

#### Related Modules

- `shutil`: High-level file operations (copy, move, remove directories).
- `glob`: Pattern matching for file names.


```
```


### Detailed Notes: Object Persistence Modules

#### What Is Object Persistence?
Object persistence refers to saving Python objects to disk (or other storage) so they can be retrieved and used later. This is useful for caching, configuration, session management, and more.

#### The `pickle` Module

- Serializes (pickles) and deserializes (unpickles) Python objects to/from byte streams.
- Supports most built-in types and user-defined classes.

```python
import pickle

data = {'x': 42, 'y': [1, 2, 3]}
# Save object to file
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Load object from file
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
print(loaded)
```

**Key Points:**
- Not secure against untrusted sources (can execute arbitrary code).
- Use for trusted data only.
- Supports custom serialization via `__getstate__` and `__setstate__`.

#### The `shelve` Module

- Provides a persistent, dictionary-like object database.
- Stores pickled objects in a file using a key-value interface.

```python
import shelve

with shelve.open('mydata') as db:
    db['numbers'] = [1, 2, 3]
    db['config'] = {'debug': True}

with shelve.open('mydata') as db:
    print(db['numbers'])
    print(db['config'])
```

**Key Points:**
- Keys must be strings.
- Values can be any picklable Python object.
- Useful for simple persistent storage without a full database.

#### The `json` Module

- Serializes Python objects to JSON format (text-based, human-readable).
- Supports basic types: dict, list, str, int, float, bool, None.

```python
import json

data = {'name': 'Alice', 'age': 30}
# Write to file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Read from file
with open('data.json', 'r') as f:
    loaded = json.load(f)
print(loaded)
```

**Key Points:**
- Only supports basic types (no custom classes).
- Good for interoperability with other languages and systems.

#### Other Persistence Options

- `csv`: For tabular data (rows/columns).
- `sqlite3`: Lightweight SQL database for structured storage.
- `configparser`: For INI-style configuration files.

#### Summary

- Use `pickle` for arbitrary Python objects (trusted data only).
- Use `shelve` for persistent key-value storage.
- Use `json` for interoperable, human-readable data.
- Choose the module based on data type, security, and interoperability needs.

#### Best Practices

- Always handle exceptions when reading/writing files.
- Avoid pickling sensitive or untrusted data.
- Consider versioning your data formats for long-term persistence.


```
```


### Detailed Notes: `time` and `datetime` Modules

#### The `time` Module

The `time` module provides functions for working with time, including timestamps, delays, and conversions.

**Common Features:**

- `time.time()`: Returns the current time as a floating-point number (seconds since the epoch).
    ```python
    import time
    print(time.time())
    ```
- `time.sleep(seconds)`: Pauses execution for the specified number of seconds.
    ```python
    time.sleep(2)
    ```
- `time.localtime([secs])`: Converts a timestamp to a struct_time in local time.
    ```python
    print(time.localtime())
    ```
- `time.strftime(format, t)`: Formats a struct_time as a string.
    ```python
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ```
- `time.gmtime([secs])`: Converts a timestamp to UTC.

**Use Cases:**
- Measuring execution time.
- Delaying code execution.
- Formatting and parsing time strings.

#### The `datetime` Module

The `datetime` module provides classes for manipulating dates and times in a more object-oriented way.

**Key Classes:**
- `datetime.datetime`: Represents date and time.
- `datetime.date`: Represents a date.
- `datetime.time`: Represents a time.
- `datetime.timedelta`: Represents a duration.

**Common Features:**

- Get current date and time:
    ```python
    from datetime import datetime
    now = datetime.now()
    print(now)
    ```
- Formatting dates:
    ```python
    print(now.strftime("%A, %d %B %Y %I:%M%p"))
    ```
- Parsing strings to dates:
    ```python
    dt = datetime.strptime("2024-06-01", "%Y-%m-%d")
    ```
- Date arithmetic:
    ```python
    from datetime import timedelta
    future = now + timedelta(days=7)
    print(future)
    ```
- Getting components:
    ```python
    print(now.year, now.month, now.day)
    ```

**Use Cases:**
- Scheduling tasks.
- Logging timestamps.
- Calculating durations and intervals.
- Formatting dates for display or storage.

#### Differences and Interoperability

- `time` is lower-level, works with timestamps and struct_time.
- `datetime` is higher-level, works with objects and supports arithmetic.
- You can convert between them using `datetime.fromtimestamp()` and `datetime.timestamp()`.

#### Best Practices

- Use `datetime` for most date/time manipulations.
- Use `time` for performance measurement and simple delays.
- Always be aware of time zones; use `datetime.timezone` or third-party libraries like `pytz` for robust handling.

#### Related Modules

- `calendar`: For calendar-related functions.
- `dateutil`: Third-party module for advanced date/time parsing and arithmetic.

```
```


### Detailed Notes: File-related Modules & Logging

#### File I/O in Python

Python provides built-in support for reading and writing files using the `open()` function.

**Basic File Operations:**
- Opening a file: `open(filename, mode)`
    - Modes: `'r'` (read), `'w'` (write), `'a'` (append), `'b'` (binary), `'x'` (exclusive creation)
- Reading:
    ```python
    with open('example.txt', 'r') as f:
        content = f.read()
    ```
- Writing:
    ```python
    with open('output.txt', 'w') as f:
        f.write("Hello, world!")
    ```
- Reading lines:
    ```python
    with open('example.txt') as f:
        for line in f:
            print(line.strip())
    ```
- Appending:
    ```python
    with open('log.txt', 'a') as f:
        f.write("New entry\n")
    ```

**Best Practices:**
- Use the `with` statement for automatic resource management.
- Always handle exceptions (`try...except`) for robust file operations.

#### The `os` and `os.path` Modules

- `os.remove(path)`: Delete a file.
- `os.rename(src, dst)`: Rename a file.
- `os.mkdir(path)`, `os.makedirs(path)`: Create directories.
- `os.path.exists(path)`: Check if a file or directory exists.
- `os.path.join()`: Build file paths in a platform-independent way.

#### The `shutil` Module

- High-level file operations:
    - `shutil.copy(src, dst)`: Copy files.
    - `shutil.move(src, dst)`: Move files or directories.
    - `shutil.rmtree(path)`: Remove directories recursively.

#### The `glob` Module

- Pattern matching for file names:
    ```python
    import glob
    files = glob.glob('*.txt')
    print(files)
    ```

#### The `logging` Module

Python’s `logging` module provides a flexible framework for emitting log messages from Python programs.

**Basic Usage:**
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")
```

**Log Levels:**
- `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`

**Advanced Features:**
- Custom log format:
    ```python
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO
    )
    ```
- Logging to a file:
    ```python
    logging.basicConfig(filename='app.log', level=logging.INFO)
    ```
- Creating loggers, handlers, and formatters for complex applications.

**Best Practices:**
- Use logging instead of print statements for production code.
- Set appropriate log levels for development and deployment.
- Rotate log files using `logging.handlers.RotatingFileHandler` for large applications.

#### Summary

- Use built-in file I/O for reading/writing files.
- Use `os`, `os.path`, `shutil`, and `glob` for advanced file and directory operations.
- Use `logging` for robust, configurable logging in scripts and applications.
- Always handle exceptions and use context managers for safe resource management.


```
```

### Detailed Notes: `re`, `numpy`, and `pandas`

#### The `re` Module (Regular Expressions)

The `re` module provides support for regular expressions, enabling pattern matching and text manipulation.

**Common Functions:**
- `re.search(pattern, string)`: Searches for the pattern anywhere in the string.
- `re.match(pattern, string)`: Matches the pattern at the start of the string.
- `re.findall(pattern, string)`: Returns all non-overlapping matches as a list.
- `re.sub(pattern, repl, string)`: Replaces occurrences of the pattern with `repl`.
- `re.split(pattern, string)`: Splits the string by the pattern.

**Example:**
```python
import re
text = "The price is 100 dollars"
match = re.search(r'\d+', text)
if match:
    print(match.group())  # 100
```

**Pattern Syntax:**
- `\d`: Digit
- `\w`: Word character
- `\s`: Whitespace
- `.`: Any character except newline
- `*`, `+`, `?`: Quantifiers

**Use Cases:**
- Data validation
- Text parsing and extraction
- Search and replace

#### The `numpy` Module (Numerical Computing)

`numpy` is the fundamental package for scientific computing with Python, providing support for arrays, matrices, and mathematical functions.

**Key Features:**
- `np.array()`: Create arrays.
- Vectorized operations for fast computation.
- Linear algebra, statistics, random number generation.

**Example:**
```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr * 2)  # [2 4 6]
matrix = np.array([[1, 2], [3, 4]])
print(np.dot(matrix, arr[:2]))  # Matrix multiplication
```

**Common Functions:**
- `np.arange(start, stop, step)`: Create sequences.
- `np.mean(arr)`, `np.std(arr)`: Statistics.
- `np.reshape(arr, shape)`: Change array shape.

**Use Cases:**
- Data analysis
- Machine learning
- Scientific simulations

#### The `pandas` Module (Data Analysis)

`pandas` is a powerful library for data manipulation and analysis, built on top of `numpy`.

**Key Data Structures:**
- `Series`: 1D labeled array.
- `DataFrame`: 2D labeled table (rows and columns).

**Example:**
```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
df['new_col'] = df['existing_col'] * 2
df.to_excel('output.xlsx')
```

**Common Operations:**
- Reading/writing CSV, Excel, JSON files.
- Filtering, grouping, aggregating data.
- Handling missing values: `df.dropna()`, `df.fillna(value)`
- Merging and joining DataFrames.

**Use Cases:**
- Data cleaning and transformation
- Exploratory data analysis
- Time series analysis

#### Summary

- Use `re` for pattern matching and text processing.
- Use `numpy` for efficient numerical computations and array operations.
- Use `pandas` for powerful, flexible data analysis and manipulation.
- These modules are essential for data science, analytics, and scientific programming in Python.


```
```


## Python Standard Modules Cheatsheet

### Decorators
- Extend/modify function/class behavior.
- Syntax: `@decorator`
- Use cases: logging, access control, memoization.
- Built-in: `@staticmethod`, `@classmethod`, `@property`
- Use `functools.wraps` to preserve metadata.

### Generators
- Functions using `yield` for lazy iteration.
- Memory-efficient for large/infinite data.
- Generator expressions: `(x for x in iterable)`
- Use `next()` to get values.
- Custom iterators: implement `__iter__` and `__next__`.

### `sys` and `os` Modules
- `sys`: Command-line args (`sys.argv`), exit (`sys.exit()`), paths (`sys.path`).
- `os`: File/directory ops (`os.listdir`, `os.remove`), env vars (`os.environ`), path utils (`os.path.join`).
- Use `os.path` for cross-platform paths.

### Object Persistence
- `pickle`: Serialize/deserialize Python objects (trusted data only).
- `shelve`: Persistent dict-like storage.
- `json`: Human-readable, interoperable format (basic types only).
- Other: `csv`, `sqlite3`, `configparser`.

### `time` and `datetime` Modules
- `time`: Timestamps (`time.time()`), delays (`time.sleep()`), formatting (`time.strftime()`).
- `datetime`: Dates/times (`datetime.now()`), arithmetic (`timedelta`), parsing/formatting.
- Prefer `datetime` for most date/time tasks.

### File I/O & Logging
- File ops: `open()`, `read()`, `write()`, context manager (`with`).
- Directory/file management: `os`, `os.path`, `shutil`, `glob`.
- Logging: `logging` module, log levels (`INFO`, `WARNING`, etc.), custom formats, file logging.

### `re`, `numpy`, and `pandas`
- `re`: Regular expressions for pattern matching (`search`, `match`, `findall`, `sub`).
- `numpy`: Arrays, vectorized math, stats, linear algebra.
- `pandas`: DataFrames, CSV/Excel I/O, filtering, grouping, missing data handling.

---

**Tip:** Use these modules for scripting, automation, data analysis, and robust application development in Python.
