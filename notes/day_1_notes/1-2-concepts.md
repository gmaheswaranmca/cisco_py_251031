### Object Based vs Object Oriented Programming in Python

#### Object Based Programming
- **Definition**: Object based programming refers to languages or paradigms that support the use of objects, but may not support all features of object oriented programming, such as inheritance and polymorphism.
- **Features**:
    - Supports encapsulation: Data and methods are bundled together as objects.
    - May lack inheritance: Objects cannot inherit properties or behaviors from other objects.
    - May lack polymorphism: Objects may not be able to take on multiple forms or interfaces.
- **Examples**: Early versions of JavaScript, Visual Basic (pre-.NET), and some scripting languages.
- **In Python**: All data types are objects, and you can create custom objects using classes. However, if you use objects without inheritance or polymorphism, you are essentially using Python in an object based way.

#### Object Oriented Programming (OOP)
- **Definition**: Object oriented programming is a paradigm that uses objects and supports key features such as encapsulation, inheritance, and polymorphism.
- **Features**:
    - **Encapsulation**: Bundling data and methods that operate on that data within objects.
    - **Inheritance**: Ability to create new classes based on existing classes, inheriting attributes and behaviors.
    - **Polymorphism**: Ability for different classes to be treated as instances of the same class through a common interface.
    - **Abstraction**: Hiding complex implementation details and exposing only necessary features.
- **In Python**:
    - Python fully supports OOP, allowing creation of classes, inheritance, method overriding, and use of abstract base classes.
    - Example:
        ```python
        class Animal:
                def speak(self):
                        pass

        class Dog(Animal):
                def speak(self):
                        return "Woof!"

        class Cat(Animal):
                def speak(self):
                        return "Meow!"
        ```
    - Here, `Dog` and `Cat` inherit from `Animal` and override the `speak` method, demonstrating inheritance and polymorphism.

#### Key Differences
| Feature         | Object Based           | Object Oriented         |
|-----------------|-----------------------|-------------------------|
| Encapsulation   | Yes                   | Yes                     |
| Inheritance     | No                    | Yes                     |
| Polymorphism    | No                    | Yes                     |
| Abstraction     | Limited               | Yes                     |

#### Summary
- **Object based** programming uses objects for encapsulation but lacks inheritance and polymorphism.
- **Object oriented** programming uses objects and supports encapsulation, inheritance, polymorphism, and abstraction.
- Python is a fully object oriented language, but can be used in an object based style if advanced features are not utilized.

```
```

### References in Python

#### What is a Reference?
- A **reference** in Python is a name that points to an object stored in memory.
- Variables in Python do not hold the actual data; they hold references to objects.
- Multiple variables can reference the same object.

#### How References Work
- When you assign a value to a variable, Python creates an object and the variable refers to it.
    ```python
    a = [1, 2, 3]
    b = a  # b now references the same list object as a
    ```
- Both `a` and `b` point to the same list in memory. Changes via one reference affect the object seen by the other.

#### Reference Counting
- Python uses **reference counting** to keep track of how many references point to an object.
- When the reference count drops to zero (no references), the object can be garbage collected.

#### Identity vs Equality
- **Identity (`is`)**: Checks if two references point to the same object.
- **Equality (`==`)**: Checks if the objects referenced have the same value.
    ```python
    x = [1, 2]
    y = x
    z = [1, 2]
    print(x is y)  # True
    print(x == z)  # True
    print(x is z)  # False
    ```

#### Mutable vs Immutable Objects
- **Mutable objects** (e.g., lists, dicts): Changes via one reference affect all references.
- **Immutable objects** (e.g., ints, strings, tuples): Any change creates a new object, and the reference is updated.

#### Passing References to Functions
- Function arguments in Python are passed by reference (object reference is passed).
    ```python
    def modify(lst):
        lst.append(4)
    nums = [1, 2, 3]
    modify(nums)
    print(nums)  # [1, 2, 3, 4]
    ```
- The function modifies the original object since both the argument and the parameter reference the same object.

#### Aliasing
- **Aliasing** occurs when multiple variables refer to the same object.
- Can lead to unintended side effects if the object is mutable.

#### Reference Cycles
- Occur when objects reference each other, forming a cycle.
- Python’s garbage collector can detect and clean up reference cycles.

#### Practical Implications
- Understanding references is crucial for managing memory, avoiding bugs, and writing efficient code.
- Be cautious with mutable objects and aliasing to prevent unexpected behavior.

#### Summary
- Python variables are references to objects, not containers of data.
- Reference management is key to understanding assignment, function calls, and object lifecycle.
- Reference counting and garbage collection help manage memory automatically.

```
```

### Memory Layout in Python

#### Overview
- Python abstracts memory management from the programmer, but understanding its memory layout helps optimize code and avoid pitfalls.
- Python objects are stored in the **heap**, while references (variable names) exist in the **stack**.

#### Python Object Structure
- Every object in Python is represented by a structure in memory, typically including:
    - **Type information**: Identifies the object's type (e.g., int, list).
    - **Reference count**: Tracks how many references point to the object.
    - **Value/data**: The actual data held by the object.

#### Memory Allocation
- **Heap Memory**: All objects (lists, dicts, user-defined objects) are allocated on the heap.
- **Stack Memory**: Local variables and references are stored on the stack, pointing to objects on the heap.

#### Example: Variable Assignment
```python
x = [1, 2, 3]
y = x
```
- `x` and `y` are references on the stack, both pointing to the same list object in the heap.

#### Immutable vs Mutable Objects
- **Immutable objects** (e.g., integers, strings, tuples):
    - Their value cannot be changed after creation.
    - Any modification results in a new object allocation.
- **Mutable objects** (e.g., lists, dicts, sets):
    - Can be changed in place without creating a new object.

#### Interning and Small Object Optimization
- Python **interns** small integers and strings for efficiency.
    - E.g., integers from -5 to 256 are pre-allocated and reused.
    - Common strings may also be interned.
- Reduces memory usage and speeds up comparisons.

#### Memory Management Techniques
- **Reference Counting**: Each object tracks the number of references to it.
- **Garbage Collection**: Python uses a cyclic garbage collector to clean up objects with zero references or those involved in reference cycles.

#### Memory Layout of Built-in Types
- **Integers**: Small integers are interned; larger integers are allocated dynamically.
- **Lists**: Implemented as dynamic arrays; resizing may allocate new memory blocks.
- **Dictionaries**: Hash tables with dynamic resizing.

#### Inspecting Memory Layout
- Use the `sys.getsizeof()` function to check the memory size of objects.
    ```python
    import sys
    print(sys.getsizeof([1, 2, 3]))  # Size in bytes
    ```
- The `id()` function returns the memory address of an object.

#### Practical Implications
- Understanding memory layout helps avoid unnecessary object creation and optimize performance.
- Be mindful of memory usage with large data structures or in memory-constrained environments.

#### Summary
- Python manages memory automatically, but objects reside in the heap and references in the stack.
- Immutable objects are reallocated on change; mutable objects are modified in place.
- Interning and garbage collection optimize memory usage and performance.
- Tools like `sys.getsizeof()` and `id()` help inspect memory details.


```
```

### Book Keeping in Python – Packages and Namespaces

#### Overview
- **Book keeping** in Python refers to the organization and management of code, modules, packages, and namespaces.
- It ensures code modularity, reusability, and prevents naming conflicts.

#### Modules
- A **module** is a single Python file (`.py`) containing definitions and statements.
- Modules allow code organization into logical units.
    ```python
    # mymodule.py
    def greet():
        print("Hello!")
    ```
- Importing modules:
    ```python
    import mymodule
    mymodule.greet()
    ```

#### Packages
- A **package** is a directory containing multiple modules and a special `__init__.py` file.
- Packages enable hierarchical structuring of modules.
    ```
    mypackage/
        __init__.py
        module1.py
        module2.py
    ```
- Importing from packages:
    ```python
    from mypackage import module1
    ```

#### Namespaces
- A **namespace** is a mapping from names to objects.
- Python uses namespaces to avoid naming conflicts and manage scope.
- Types of namespaces:
    - **Local Namespace**: Inside a function.
    - **Global Namespace**: At the module level.
    - **Built-in Namespace**: Provided by Python itself (e.g., `len`, `print`).

#### Scope Resolution (LEGB Rule)
- Python resolves names using the **LEGB** rule:
    - **L**ocal: Names inside the current function.
    - **E**nclosing: Names in enclosing functions (nested).
    - **G**lobal: Names at the module level.
    - **B**uilt-in: Names in the built-in namespace.

#### Import System
- Python’s import system manages module and package loading.
- Supports absolute and relative imports.
    - **Absolute import**: `import mypackage.module1`
    - **Relative import**: `from . import module2`

#### `__init__.py` File
- Marks a directory as a Python package.
- Can execute initialization code for the package.

#### Aliasing and Name Clashes
- Aliasing helps avoid name clashes:
    ```python
    import numpy as np
    ```
- Use `from ... import ... as ...` for specific names.

#### Practical Implications
- Proper use of packages and namespaces keeps code organized and maintainable.
- Avoids naming conflicts in large projects.
- Facilitates code reuse and distribution.

#### Summary
- Modules and packages organize Python code for clarity and reuse.
- Namespaces prevent naming conflicts and manage scope.
- The import system and `__init__.py` enable modular programming and package management.
- Understanding book keeping is essential for scalable Python development.

```
```

### Shallow Copy vs Deep Copy in Python

#### Overview
- Copying objects is essential when you want to duplicate data structures without affecting the original.
- Python provides two main ways to copy objects: **shallow copy** and **deep copy**.

#### Shallow Copy
- A **shallow copy** creates a new object but does not recursively copy nested objects.
- The new object contains references to the same nested objects as the original.
- Changes to nested objects affect both the original and the copy.
- Use the `copy()` method (for lists, dicts) or the `copy` module:
    ```python
    import copy
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    shallow[0].append(99)
    print(original)  # [[1, 2, 99], [3, 4]]
    print(shallow)   # [[1, 2, 99], [3, 4]]
    ```

#### Deep Copy
- A **deep copy** creates a new object and recursively copies all nested objects.
- The copy is completely independent of the original; changes to nested objects do not affect the original.
- Use `copy.deepcopy()`:
    ```python
    import copy
    original = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original)
    deep[0].append(99)
    print(original)  # [[1, 2], [3, 4]]
    print(deep)      # [[1, 2, 99], [3, 4]]
    ```

#### When to Use
- **Shallow copy**: When you want a new container but shared nested objects are acceptable.
- **Deep copy**: When you need a completely independent copy, especially for complex, nested structures.

#### Copying Built-in Types
- Immutable types (int, str, tuple) do not need copying; assignment creates new references.
- Mutable types (list, dict, set) require careful copying to avoid unintended side effects.

#### Limitations and Considerations
- Deep copying can be slow for large or deeply nested objects.
- Custom objects may need to define their own copy behavior via `__copy__` and `__deepcopy__` methods.

#### Summary
- Shallow copy duplicates the outer object, sharing nested objects.
- Deep copy duplicates the entire object hierarchy, making all objects independent.
- Use the `copy` module for reliable copying of complex objects.
- Understanding copying is crucial for managing data integrity and avoiding bugs in Python programs.

```
```

### Deep Dive into Objects in Memory

#### Python Object Model
- Every value in Python is an object, including numbers, strings, functions, and classes.
- Objects are instances of types (classes), and each object has a unique identity, type, and value.

#### Object Structure
- Internally, each object contains:
    - **Reference count**: Tracks how many references point to the object.
    - **Type pointer**: Points to the object's type (class).
    - **Value/data**: The actual data stored by the object.

#### Object Identity
- The `id()` function returns the unique identity (memory address) of an object.
    ```python
    a = [1, 2, 3]
    print(id(a))
    ```

#### Object Lifecycle
- **Creation**: Objects are created when a value is assigned or instantiated.
- **Modification**: Mutable objects can be changed in place; immutable objects require new allocations.
- **Destruction**: When an object’s reference count drops to zero, it becomes eligible for garbage collection.

#### Memory Allocation
- Objects are allocated on the heap, managed by Python’s memory manager.
- The memory manager handles allocation, deallocation, and optimization (e.g., interning).

#### Object References and Aliasing
- Multiple variables can reference the same object, leading to aliasing.
- Changes via one reference affect all references to the same object (for mutable types).

#### Inspecting Objects in Memory
- Use `sys.getsizeof()` to check the memory footprint of an object.
- Use `gc` module to inspect objects tracked by the garbage collector.
    ```python
    import gc
    print(gc.get_objects())
    ```

#### Object Graphs and Reference Cycles
- Objects can reference other objects, forming complex graphs.
- Reference cycles (objects referencing each other) can prevent reference counts from reaching zero.
- Python’s cyclic garbage collector detects and cleans up such cycles.

#### Custom Objects
- User-defined classes create custom objects with attributes and methods.
- The `__dict__` attribute stores an object’s attributes in a dictionary.
    ```python
    class MyClass:
        def __init__(self):
            self.x = 10
    obj = MyClass()
    print(obj.__dict__)  # {'x': 10}
    ```

#### Slots for Memory Optimization
- Using `__slots__` in a class restricts attribute creation and saves memory by avoiding per-object dictionaries.
    ```python
    class MyClass:
        __slots__ = ['x']
        def __init__(self):
            self.x = 10
    ```

#### Practical Implications
- Understanding objects in memory helps optimize performance and avoid bugs related to aliasing and memory leaks.
- Tools like `id()`, `sys.getsizeof()`, and the `gc` module aid in debugging and profiling memory usage.

#### Summary
- Python objects have identity, type, and value, and are managed on the heap.
- Reference counting and garbage collection handle object lifecycle.
- Inspecting and optimizing object memory usage is key for efficient Python programming.
- Customization via `__dict__` and `__slots__` allows control over object memory footprint.

```
```

### Garbage Collector in Python

#### Overview
- The **garbage collector** in Python is responsible for automatic memory management, reclaiming memory occupied by objects that are no longer in use.
- It prevents memory leaks and ensures efficient use of resources.

#### Reference Counting
- Python primarily uses **reference counting** to track how many references point to each object.
- When an object’s reference count drops to zero, its memory is immediately reclaimed.
    ```python
    import sys
    a = []
    print(sys.getrefcount(a))  # Shows the reference count for object 'a'
    ```

#### Cyclic Garbage Collection
- Reference counting alone cannot handle **reference cycles** (objects referencing each other).
- Python’s **cyclic garbage collector** (in the `gc` module) detects and collects objects involved in cycles.
- The collector periodically scans for unreachable objects and frees their memory.

#### The `gc` Module
- Provides tools to interact with the garbage collector.
    - `gc.collect()`: Manually trigger garbage collection.
    - `gc.get_objects()`: List all objects tracked by the collector.
    - `gc.set_debug()`: Enable debugging output for garbage collection.
    ```python
    import gc
    gc.collect()  # Force a garbage collection
    ```

#### Generational Collection
- Python’s garbage collector uses **generational collection**:
    - Objects are grouped into generations based on their lifespan.
    - Younger generations are collected more frequently.
    - Older generations are collected less often, optimizing performance.

#### Customization and Control
- You can enable/disable garbage collection with `gc.enable()` and `gc.disable()`.
- Useful for performance tuning in specific scenarios (e.g., real-time applications).

#### Weak References
- The `weakref` module allows creation of **weak references** that do not increase reference count.
- Useful for caching and tracking objects without preventing their collection.

#### Practical Implications
- Most Python programs do not need manual memory management; the garbage collector handles it automatically.
- Understanding garbage collection helps avoid memory leaks, especially with complex object graphs and cycles.
- Manual intervention may be needed in performance-critical or long-running applications.

#### Summary
- Python’s garbage collector combines reference counting and cyclic collection to manage memory automatically.
- The `gc` and `weakref` modules provide advanced control and inspection capabilities.
- Proper understanding of garbage collection is essential for writing robust, memory-efficient Python code.



```
```

### Python Concepts Cheatsheet

#### Object Based vs Object Oriented
- **Object Based**: Uses objects for encapsulation; lacks inheritance/polymorphism.
- **Object Oriented**: Supports encapsulation, inheritance, polymorphism, abstraction.

#### References
- Variables hold references to objects, not the objects themselves.
- Multiple variables can reference the same object (aliasing).
- Reference counting manages object lifecycle.

#### Memory Layout
- Objects stored on the heap; references on the stack.
- Immutable objects are reallocated on change; mutable objects are modified in place.
- Interning optimizes small objects.

#### Book Keeping – Packages/Namespaces
- **Modules**: Single `.py` files.
- **Packages**: Directories with `__init__.py`.
- **Namespaces**: Manage scope and avoid name clashes (LEGB rule).
- Import system enables modular code.

#### Shallow Copy vs Deep Copy
- **Shallow Copy**: Copies outer object; nested objects are shared.
- **Deep Copy**: Recursively copies all nested objects; fully independent.
- Use `copy` module for copying.

#### Deep Dive into Objects in Memory
- Objects have identity, type, value; managed on the heap.
- Reference count, type pointer, and value/data are core components.
- Use `id()`, `sys.getsizeof()`, and `gc` for inspection.
- `__dict__` and `__slots__` optimize custom objects.

#### Garbage Collector
- Combines reference counting and cyclic collection.
- `gc` module for manual control and inspection.
- Generational collection optimizes performance.
- Weak references allow tracking without preventing collection.

---
**Tip**: Understanding these concepts helps write efficient, maintainable, and bug-free Python code.
