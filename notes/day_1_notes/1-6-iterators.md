### Iterator Protocol

The iterator protocol in Python enables objects to be iterated over (looped through) using constructs like the `for` loop. It consists of two main components: **Iterable** and **Iterator**.

#### Iterable
- An object is **iterable** if it implements the `__iter__()` method, which returns an iterator.
- Examples: lists, tuples, strings, dictionaries, sets.

#### Iterator
- An **iterator** is an object with a `__next__()` method, which returns the next item in the sequence.
- When there are no more items, `__next__()` raises a `StopIteration` exception.

#### foreach Loop (for loop)
- The `for` loop in Python uses the iterator protocol internally.
- When you write `for item in iterable:`, Python calls `iter(iterable)` to get an iterator, then repeatedly calls `next(iterator)` until `StopIteration` is raised.

#### StopIteration
- This exception signals that there are no further items produced by the iterator.
- The `for` loop catches this exception to end the loop gracefully.

#### `next` Function
- The built-in `next()` function retrieves the next item from an iterator.
- Syntax: `next(iterator[, default])`
- If the iterator is exhausted, `StopIteration` is raised unless a default value is provided.

#### Example

```python
s = "hello"
it = iter(s)  # Get iterator from string

print(next(it))  # 'h'
print(next(it))  # 'e'
# ... continues until StopIteration is raised
```

#### Custom Iterator Example

```python
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for num in Counter(1, 3):
    print(num)  # 1, 2, 3
```

#### Types of Iterators
- **Sequence iterators**: Iterate over sequences like lists, tuples, strings.
- **Dictionary iterators**: Iterate over keys, values, or items.
- **Custom iterators**: User-defined classes implementing `__iter__()` and `__next__()`.

#### Summary Table

| Term           | Description                                      |
|----------------|--------------------------------------------------|
| Iterable       | Object with `__iter__()` method                  |
| Iterator       | Object with `__next__()` method                  |
| StopIteration  | Exception to signal end of iteration             |
| next()         | Built-in function to get next item from iterator |


```
```

### Different Types of Iterators

Python provides several built-in iterators for different data structures, and you can also create custom iterators. Here are the main types:

#### 1. Sequence Iterators
- Used for sequences like lists, tuples, and strings.
- Iterate over elements in order.
- Example:
    ```python
    lst = [1, 2, 3]
    it = iter(lst)
    print(next(it))  # 1
    print(next(it))  # 2
    ```

#### 2. String Iterators
- Strings are iterable; their iterator yields one character at a time.
- Example:
    ```python
    s = "abc"
    it = iter(s)
    print(next(it))  # 'a'
    print(next(it))  # 'b'
    ```

#### 3. Dictionary Iterators
- Dictionaries provide iterators for keys, values, and items.
- Examples:
    ```python
    d = {'x': 1, 'y': 2}
    for key in d:        # Iterates over keys
            print(key)
    for value in d.values():  # Iterates over values
            print(value)
    for item in d.items():    # Iterates over (key, value) pairs
            print(item)
    ```

#### 4. Set Iterators
- Sets are unordered collections; their iterator yields elements in arbitrary order.
- Example:
    ```python
    s = {10, 20, 30}
    for item in s:
            print(item)
    ```

#### 5. File Object Iterators
- File objects are iterable; each iteration yields a line from the file.
- Example:
    ```python
    with open('file.txt') as f:
            for line in f:
                    print(line)
    ```

#### 6. Enumerate Iterator
- `enumerate()` returns an iterator that yields pairs of (index, value).
- Example:
    ```python
    for idx, val in enumerate(['a', 'b', 'c']):
            print(idx, val)
    ```

#### 7. Zip Iterator
- `zip()` returns an iterator that aggregates elements from multiple iterables.
- Example:
    ```python
    for a, b in zip([1, 2], ['x', 'y']):
            print(a, b)
    ```

#### 8. Custom Iterators
- You can define your own iterator by implementing `__iter__()` and `__next__()` methods.
- Useful for complex iteration logic.

#### 9. Generator Iterators
- Generators are functions that yield values using `yield`.
- They produce iterator objects.
- Example:
    ```python
    def countdown(n):
            while n > 0:
                    yield n
                    n -= 1
    for num in countdown(3):
            print(num)
    ```

#### Summary Table

| Iterator Type      | Description                                 | Example Usage                |
|--------------------|---------------------------------------------|------------------------------|
| Sequence           | Iterates over lists, tuples, strings        | `iter([1,2,3])`              |
| Dictionary         | Iterates over keys, values, items           | `dict.items()`               |
| Set                | Iterates over set elements                  | `for x in set`               |
| File Object        | Iterates over lines in a file               | `for line in file`           |
| Enumerate          | Index-value pairs from iterable             | `enumerate(list)`            |
| Zip                | Parallel iteration over multiple iterables  | `zip(list1, list2)`          |
| Custom             | User-defined iteration logic                | Custom class                 |
| Generator          | Function-based, yields values               | `def gen(): yield ...`       |


```
```

### Iterators in Python: Cheatsheet

#### Key Concepts
- **Iterable**: Object with `__iter__()` method; can be looped over.
- **Iterator**: Object with `__next__()` method; produces items one at a time.
- **Iterator Protocol**: Used by `for` loops; calls `iter()` and repeatedly `next()`.
- **StopIteration**: Exception raised when iterator is exhausted.
- **next()**: Built-in function to get next item from iterator.

#### Common Iterator Types
| Type         | Description                        | Example Usage                |
|--------------|------------------------------------|------------------------------|
| Sequence     | Lists, tuples, strings             | `iter([1,2,3])`              |
| Dictionary   | Keys, values, items                | `dict.items()`               |
| Set          | Unordered elements                 | `for x in set`               |
| File Object  | Lines in a file                    | `for line in file`           |
| Enumerate    | Index-value pairs                  | `enumerate(list)`            |
| Zip          | Parallel iteration                 | `zip(list1, list2)`          |
| Custom       | User-defined logic                 | Custom class                 |
| Generator    | Function yielding values           | `def gen(): yield ...`       |

#### Example Usage
```python
# Sequence iterator
lst = [1, 2, 3]
it = iter(lst)
print(next(it))  # 1

# Custom iterator
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        self.current += 1
        return self.current - 1

for num in Counter(1, 3):
    print(num)  # 1, 2, 3
```

#### Quick Reference
- Use `for item in iterable:` for automatic iteration.
- Use `iter(obj)` to get an iterator.
- Use `next(iterator)` to get next item.
- Implement `__iter__()` and `__next__()` for custom iterators.
- Generators use `yield` to produce values.
