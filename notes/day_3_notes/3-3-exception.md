## Introduction to Exceptions

Exceptions are events that disrupt the normal flow of a program's execution. They typically occur when an error or unexpected condition arises, such as dividing by zero, accessing a non-existent file, or running out of memory. Exception handling provides a structured way to detect, manage, and recover from such errors, improving program reliability and user experience.

### Key Concepts

- **Error vs Exception**: Errors are serious problems that a program should not try to handle (e.g., hardware failure), while exceptions are conditions that a program can anticipate and manage (e.g., invalid input).
- **Exception Objects**: When an exception occurs, an object representing the error is created and thrown. This object contains information about the error type and context.
- **Exception Propagation**: If an exception is not handled where it occurs, it propagates up the call stack until it is caught or the program terminates.

### Benefits of Exception Handling

- **Separation of Error Handling Code**: Keeps normal logic separate from error handling, making code cleaner and easier to maintain.
- **Graceful Recovery**: Allows programs to recover from errors and continue execution or terminate gracefully.
- **Debugging Support**: Provides detailed error information, aiding in debugging and troubleshooting.

### Common Exception Scenarios

- Invalid user input
- File not found or inaccessible
- Network errors
- Resource exhaustion (memory, disk space)
- Arithmetic errors (division by zero)

Exception handling is a fundamental concept in modern programming languages, enabling robust and maintainable software development.


```
```

## Detecting and Handling Exceptions

Exception handling allows programs to detect errors and respond appropriately, preventing crashes and enabling graceful recovery. Most modern languages provide constructs for catching and managing exceptions.

### Exception Handling Constructs

- **Try-Catch Blocks**: Code that may raise an exception is placed inside a `try` block. If an exception occurs, control transfers to the corresponding `catch` (or `except`) block, where the error is handled.
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Error:", e)
    ```
    ```java
    try {
        int result = 10 / 0;
    } catch (ArithmeticException e) {
        System.out.println("Error: " + e.getMessage());
    }
    ```

- **Finally Block**: Used to specify code that should run regardless of whether an exception occurred, often for cleanup tasks.
    ```python
    try:
        f = open('file.txt')
    except FileNotFoundError:
        print("File not found.")
    finally:
        print("Closing resources.")
    ```

### Exception Matching

- Exceptions are matched by type. More specific exceptions should be caught before general ones.
- Multiple exception types can be handled using multiple `catch`/`except` clauses.

### Best Practices

- Catch only exceptions you can handle meaningfully.
- Avoid catching generic exceptions unless necessary.
- Always clean up resources (files, network connections) in a `finally` block or using context managers.

### Propagation and Re-throwing

- If an exception is not caught, it propagates up the call stack.
- Exceptions can be re-thrown to higher levels for handling.
    ```python
    try:
        risky_operation()
    except Exception as e:
        log_error(e)
        raise  # re-throws the exception
    ```

### Example Workflow

1. Code executes in a `try` block.
2. If an exception occurs, control moves to the matching `catch`/`except` block.
3. Optional `finally` block executes for cleanup.
4. If not handled, the exception propagates up and may terminate the program.

Effective exception handling improves program robustness, prevents resource leaks, and enhances user experience.

```
```

## Exceptions as Strings and Classes

In many programming languages, exceptions can be represented as either strings or classes, with modern languages favoring class-based exceptions for greater flexibility and structure.

### String-Based Exceptions

- **Early Approach**: Some older languages (e.g., early Python versions) allowed exceptions to be raised as simple strings.
    ```python
    raise "An error occurred"
    ```
- **Limitations**:
    - Lack of structure and type information.
    - Difficult to distinguish between different error types.
    - Harder to catch specific errors reliably.

### Class-Based Exceptions

- **Modern Standard**: Most languages now use exception classes, which inherit from a base exception type.
    ```python
    class MyError(Exception):
        pass

    raise MyError("Something went wrong")
    ```
    ```java
    public class MyException extends Exception {
        public MyException(String message) {
            super(message);
        }
    }
    throw new MyException("Custom error");
    ```
- **Advantages**:
    - **Type Safety**: Enables catching specific exception types.
    - **Extensibility**: Custom exception classes can include additional attributes and methods.
    - **Hierarchy**: Exceptions can be organized in a class hierarchy, allowing for broad or fine-grained error handling.
    - **Rich Information**: Exception objects can carry detailed error messages, codes, and context.

### Exception Attributes

- Exception classes often include attributes such as:
    - Error message
    - Error code
    - Stack trace
    - Contextual data

### Catching Exceptions by Type

- Handlers can catch exceptions based on their class, enabling precise control.
    ```python
    try:
        risky_operation()
    except MyError as e:
        print("Caught custom error:", e)
    except Exception as e:
        print("Caught general error:", e)
    ```

### Best Practices

- Prefer class-based exceptions for maintainability and clarity.
- Use inheritance to create meaningful exception hierarchies.
- Include relevant information in custom exception classes to aid debugging.

Class-based exceptions are now the norm, providing robust mechanisms for error detection, handling, and reporting in modern software development.


```
```


## Raising Exceptions

Raising exceptions is the process of explicitly signaling that an error or unexpected condition has occurred in a program. This allows developers to interrupt normal execution and transfer control to error-handling code.

### How to Raise Exceptions

- **Using Language Constructs**: Most languages provide a keyword for raising exceptions (`raise` in Python, `throw` in Java/C++).

    ```python
    raise ValueError("Invalid value provided")
    ```

    ```java
    throw new IllegalArgumentException("Invalid argument");
    ```

- **Custom Messages**: Exceptions can include descriptive messages to clarify the error.

### When to Raise Exceptions

- When invalid input or state is detected.
- When a function cannot fulfill its contract.
- To enforce constraints or business rules.
- To signal resource exhaustion or system errors.

### Raising Built-in vs Custom Exceptions

- **Built-in Exceptions**: Use standard exceptions for common error types (e.g., `ValueError`, `TypeError`).
- **Custom Exceptions**: Raise user-defined exceptions for domain-specific errors.

### Re-raising Exceptions

- Sometimes, after handling part of an error, you may want to re-raise it for higher-level handling.

    ```python
    try:
        process_data()
    except Exception as e:
        log_error(e)
        raise  # re-raises the current exception
    ```

### Best Practices

- Raise exceptions only for exceptional conditions, not for normal control flow.
- Provide clear, informative messages.
- Use specific exception types to aid error handling and debugging.

Raising exceptions is essential for robust error signaling, enabling programs to detect, report, and recover from unexpected conditions in a controlled manner.


```
```


## Creating User-Defined Exceptions

Python allows developers to define custom exception classes to represent application-specific error conditions. This enhances code clarity and enables precise error handling.

### Defining Custom Exceptions

- Custom exceptions are typically subclasses of the built-in `Exception` class or its derivatives.
    ```python
    class MyCustomError(Exception):
        pass
    ```

- You can add custom attributes and methods to provide additional context.
    ```python
    class ValidationError(Exception):
        def __init__(self, message, field):
            super().__init__(message)
            self.field = field
    ```

### Raising User-Defined Exceptions

- Use the `raise` statement to signal a custom exception.
    ```python
    def validate_age(age):
        if age < 0:
            raise ValidationError("Age cannot be negative", "age")
    ```

### Catching Custom Exceptions

- Handle custom exceptions using `except` blocks.
    ```python
    try:
        validate_age(-5)
    except ValidationError as e:
        print(f"Validation error in field '{e.field}': {e}")
    ```

### Exception Hierarchies

- Organize custom exceptions in a hierarchy for structured error handling.
    ```python
    class AppError(Exception):
        pass

    class DatabaseError(AppError):
        pass

    class NetworkError(AppError):
        pass
    ```

### Best Practices

- Name custom exceptions with the `Error` suffix for clarity.
- Inherit from `Exception` or a relevant built-in exception.
- Provide meaningful messages and attributes to aid debugging.
- Document custom exceptions for maintainability.

User-defined exceptions make error handling more expressive and tailored to the application's needs, improving code robustness and readability.


```
```


## Standard Exceptions

Python provides a rich set of built-in exception classes to handle common error conditions. These standard exceptions cover a wide range of scenarios, making error handling consistent and predictable.

### Common Built-in Exceptions

- **Exception**: The base class for all built-in exceptions.
- **ValueError**: Raised when a function receives an argument of the correct type but inappropriate value.
    ```python
    int("abc")  # Raises ValueError
    ```
- **TypeError**: Raised when an operation or function is applied to an object of inappropriate type.
    ```python
    len(5)  # Raises TypeError
    ```
- **IndexError**: Raised when a sequence subscript is out of range.
    ```python
    lst = [1, 2]
    print(lst[5])  # Raises IndexError
    ```
- **KeyError**: Raised when a dictionary key is not found.
    ```python
    d = {"a": 1}
    print(d["b"])  # Raises KeyError
    ```
- **ZeroDivisionError**: Raised when dividing by zero.
    ```python
    10 / 0  # Raises ZeroDivisionError
    ```
- **FileNotFoundError**: Raised when a file or directory is requested but doesn’t exist.
    ```python
    open("nofile.txt")  # Raises FileNotFoundError
    ```
- **AttributeError**: Raised when an attribute reference or assignment fails.
    ```python
    "abc".not_a_method()  # Raises AttributeError
    ```
- **ImportError**: Raised when an import statement fails to find the module definition.
    ```python
    import non_existent_module  # Raises ImportError
    ```

### Exception Hierarchy

- All standard exceptions inherit from `BaseException`, with `Exception` as the main subclass for most errors.
- Specialized exceptions inherit from `Exception` for specific error types.

### Handling Standard Exceptions

- Catch specific exceptions to handle known error conditions.
    ```python
    try:
        result = int("abc")
    except ValueError as e:
        print("Conversion error:", e)
    ```

- Use multiple `except` clauses for different exception types.

### Best Practices

- Prefer catching specific exceptions over the generic `Exception`.
- Refer to the [Python documentation](https://docs.python.org/3/library/exceptions.html) for a complete list of built-in exceptions.
- Use standard exceptions for common error scenarios to ensure code clarity and maintainability.

Standard exceptions provide a robust foundation for error handling, allowing developers to write reliable and readable Python code.


```
```


## Errors and Exception Handling Cheatsheet (Python)

### Introduction to Exceptions
- **Exception**: Event disrupting normal program flow.
- **Error vs Exception**: Errors are unrecoverable; exceptions can be handled.
- **Benefits**: Cleaner code, graceful recovery, better debugging.

### Detecting and Handling Exceptions
- Use `try`, `except`, and `finally` blocks.
    ```python
    try:
        # risky code
    except ExceptionType as e:
        # handle error
    finally:
        # cleanup
    ```
- Catch specific exceptions; avoid catching generic ones.
- Exceptions propagate if not handled.

### Exceptions as Strings and Classes
- **String-based**: Outdated, lacks structure.
- **Class-based**: Preferred; enables type safety, extensibility, and rich error info.
    ```python
    class MyError(Exception): pass
    raise MyError("message")
    ```

### Raising Exceptions
- Use `raise` to signal errors.
    ```python
    raise ValueError("Invalid value")
    ```
- Raise built-in or custom exceptions.
- Re-raise with `raise` for higher-level handling.

### Creating User-Defined Exceptions
- Subclass `Exception` for custom errors.
    ```python
    class ValidationError(Exception):
        def __init__(self, msg, field): ...
    ```
- Add attributes/methods for context.
- Use meaningful names and document usage.

### Standard Exceptions
- Common built-ins: `ValueError`, `TypeError`, `IndexError`, `KeyError`, `ZeroDivisionError`, `FileNotFoundError`, `AttributeError`, `ImportError`.
- Catch specific exceptions for clarity.
    ```python
    try:
        int("abc")
    except ValueError as e:
        print(e)
    ```
- Refer to [Python docs](https://docs.python.org/3/library/exceptions.html) for full list.

---
**Best Practices**
- Handle only exceptions you can manage.
- Clean up resources in `finally` or with context managers.
- Prefer class-based and specific exceptions.
- Provide clear error messages.

