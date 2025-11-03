### Python Implementations

#### CPython
- The default and most widely used implementation of Python.
- Written in C; executes Python code by compiling it to bytecode and interpreting it.
- Supports most Python libraries and extensions.
- Official reference implementation maintained by the Python Software Foundation.
- Compatible with C/C++ extensions via the Python C API.

#### Jython
- Python implementation written in Java.
- Allows seamless integration with Java libraries and applications.
- Compiles Python code to Java bytecode, which runs on the Java Virtual Machine (JVM).
- Useful for projects requiring interoperability with Java.
- May lag behind CPython in supporting the latest Python features.

#### IronPython
- Implementation of Python for the .NET framework.
- Written in C#; integrates with .NET libraries and applications.
- Compiles Python code to .NET Intermediate Language (IL).
- Suitable for Windows environments and .NET development.
- Some CPython extensions may not be compatible.

#### PyPy
- Python implementation focused on speed and efficiency.
- Written in RPython (a subset of Python).
- Features a Just-In-Time (JIT) compiler for faster execution.
- Highly compatible with CPython, but some C extensions may not work.
- Often used for performance-critical applications.

#### Stackless Python
- Variant of CPython designed for concurrency and scalability.
- Removes reliance on the C call stack, enabling lightweight microthreads (tasklets).
- Useful for applications requiring massive concurrency, such as games and network servers.
- Maintains compatibility with most CPython features and libraries.
- Not as widely adopted as other implementations.

```
```

### Python 2 vs Python 3: Feature Differences

#### Print Statement vs Print Function
- Python 2: `print "Hello"`
- Python 3: `print("Hello")` (print is now a function)

#### Integer Division
- Python 2: `5 / 2` results in `2` (integer division)
- Python 3: `5 / 2` results in `2.5` (true division)
- Use `//` for integer division in both versions.

#### Unicode Support
- Python 2: Strings are ASCII by default; Unicode strings require a `u` prefix (`u"hello"`).
- Python 3: All strings are Unicode by default.

#### xrange vs range
- Python 2: `range()` returns a list; `xrange()` returns an iterator.
- Python 3: `range()` returns an iterator; `xrange()` is removed.

#### Input Function
- Python 2: `input()` evaluates input as code; `raw_input()` reads input as a string.
- Python 3: `input()` reads input as a string; `raw_input()` is removed.

#### Exception Syntax
- Python 2: `except Exception, e:`
- Python 3: `except Exception as e:`

#### Iterating Dictionaries
- Python 2: `dict.items()`, `dict.keys()`, `dict.values()` return lists.
- Python 3: These methods return view objects (iterators).

#### Removal of Old Features
- Python 3 removes deprecated modules and functions (e.g., `has_key()` for dictionaries, `cmp()` for sorting).

#### Standard Library Changes
- Many modules have been reorganized or renamed (e.g., `urllib`, `queue`).

#### Function Annotations and Type Hints
- Python 3 introduces function annotations and type hints for better code clarity.

#### Syntax Changes
- Python 3 enforces new syntax rules (e.g., only one way to define classes, no implicit relative imports).

#### Compatibility
- Python 2 code may not run in Python 3 without modification.
- Tools like `2to3` help convert Python 2 code to Python 3.

#### End of Life
- Python 2 reached end-of-life on January 1, 2020; Python 3 is actively maintained and developed.

### Python 2 vs Python 3: Key Differences (Tabular Form)

| Feature                  | Python 2                                  | Python 3                                  |
|--------------------------|-------------------------------------------|-------------------------------------------|
| Print                    | `print "Hello"` (statement)               | `print("Hello")` (function)               |
| Division                 | `5 / 2` → `2` (integer division)          | `5 / 2` → `2.5` (true division)           |
| Unicode Strings          | ASCII by default; `u"hello"` for Unicode  | Unicode by default                        |
| Range/xrange             | `range()` returns list; `xrange()` exists | `range()` returns iterator; no `xrange()` |
| Input                    | `input()` evaluates code; `raw_input()`   | `input()` reads string; no `raw_input()`  |
| Exception Handling       | `except Exception, e:`                    | `except Exception as e:`                  |
| Dict Iteration           | `dict.items()`, `dict.keys()` → lists     | Return view objects (iterators)           |
| Deprecated Features      | Some old features remain                  | Many removed (e.g., `has_key()`)          |
| Standard Library         | Older module names/structure              | Modules reorganized/renamed               |
| Function Annotations     | Not available                             | Supported                                 |
| Syntax                   | Multiple class definitions, imports       | Unified syntax, stricter rules            |
| Compatibility            | Not compatible with Python 3              | Not compatible with Python 2              |
| End of Life              | Ended Jan 1, 2020                         | Actively maintained                       |

```
```

### Python Programming Cheatsheet

#### Python Implementations
- **CPython**: Default, written in C, supports most libraries, C/C++ extensions.
- **Jython**: Written in Java, runs on JVM, integrates with Java libraries.
- **IronPython**: For .NET, written in C#, integrates with .NET libraries.
- **PyPy**: Focused on speed, JIT compiler, highly compatible, some C extensions may not work.
- **Stackless Python**: Concurrency-focused, supports microthreads, compatible with CPython.

#### Python 2 vs Python 3 Key Differences
- **Print**: Python 2 uses statement, Python 3 uses function.
- **Division**: Python 2: integer division by default; Python 3: true division.
- **Strings**: Python 2: ASCII by default; Python 3: Unicode by default.
- **Range/xrange**: Python 2: `range()` (list), `xrange()` (iterator); Python 3: `range()` (iterator).
- **Input**: Python 2: `input()` evaluates, `raw_input()` for strings; Python 3: `input()` for strings.
- **Exceptions**: Python 2: `except Exception, e`; Python 3: `except Exception as e`.
- **Dict Iteration**: Python 2: returns lists; Python 3: returns iterators.
- **Deprecated Features**: Python 3 removes many old features.
- **Standard Library**: Python 3 reorganized/renamed modules.
- **Function Annotations**: Available in Python 3.
- **Syntax**: Python 3 enforces stricter, unified syntax.
- **End of Life**: Python 2 ended Jan 2020; Python 3 is current.
