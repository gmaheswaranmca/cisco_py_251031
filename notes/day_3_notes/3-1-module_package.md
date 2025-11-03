## Modular Development – Modules & Packages

### Creating Modules
- A **module** is a file containing Python definitions and statements. The file name is the module name with the suffix `.py`.
- To create a module, simply write your functions, classes, or variables in a `.py` file.
- Example:  
    ```python
    # mymodule.py
    def greet(name):
            print(f"Hello, {name}!")
    ```
- Modules can be imported into other Python files using the `import` statement.

### Variable Scope
- Variables defined inside a module have **module-level scope**.
- **Global variables** in a module are accessible throughout that module.
- **Local variables** are defined within functions/classes and are only accessible there.
- The `global` and `nonlocal` keywords can be used to modify variable scope.

### Understanding Namespaces
- A **namespace** is a mapping from names to objects.
- Each module has its own namespace.
- Namespaces help avoid naming conflicts by isolating identifiers.
- Python uses different namespaces: local, enclosing, global, and built-in.

### Importing Modules and Module Attributes
- Use `import module_name` to import an entire module.
- Use `from module_name import attribute` to import specific attributes (functions, classes, variables).
- Use `as` to alias modules or attributes for convenience.
- Example:
    ```python
    import math
    from math import sqrt
    import numpy as np
    ```

### Module Hierarchy
- Modules can be organized into **packages** (directories containing an `__init__.py` file).
- Packages allow hierarchical structuring of modules.
- Example structure:
    ```
    mypackage/
            __init__.py
            module1.py
            module2.py
            subpackage/
                    __init__.py
                    submodule.py
    ```
- Importing from packages uses dot notation: `import mypackage.module1`

## Notes on Creating Modules
- Choose descriptive names for your module files.
- Place related functions, classes, and variables together for maintainability.
- Document your module with comments and docstrings.
- Test your module independently before importing into other projects.
- Use relative or absolute imports when working with packages.
- Avoid circular imports by structuring dependencies carefully.
- Consider using `__all__` in your module to define the public API.
- Example:
    ```python
    # mymodule.py
    __all__ = ['greet']

    def greet(name):
            print(f"Hello, {name}!")
    ```


## Notes on Variable Scope

- **Scope** refers to the region of a program where a variable is accessible.
- Python uses the LEGB rule to resolve variable names:
    - **Local**: Names assigned within a function (not declared global/nonlocal).
    - **Enclosing**: Names in the local scope of any enclosing functions (nested functions).
    - **Global**: Names assigned at the top-level of a module or declared global in a function.
    - **Built-in**: Names preassigned in Python (e.g., `len`, `print`).
- **Global variables** are defined at the module level and accessible throughout the module.
- **Local variables** are defined inside functions/classes and only accessible within those blocks.
- The `global` keyword allows modification of global variables inside functions.
    ```python
    count = 0
    def increment():
        global count
        count += 1
    ```
- The `nonlocal` keyword allows modification of variables in the enclosing (non-global) scope in nested functions.
    ```python
    def outer():
        x = 10
        def inner():
            nonlocal x
            x += 5
        inner()
        print(x)  # Output: 15
    ```
- Variables in different modules have separate namespaces, preventing conflicts.
- Avoid excessive use of global variables to maintain modularity and reduce side effects.
- Use function parameters and return values to pass data instead of relying on global scope.
- Understanding scope is crucial for debugging, avoiding name clashes, and writing maintainable code.

```
```

## Notes on Understanding Namespaces

- A **namespace** is a container that holds a collection of identifiers (names) and their corresponding objects.
- Namespaces help organize code and prevent naming conflicts by isolating variable/function/class names.
- Python has several types of namespaces:
    - **Built-in namespace**: Contains built-in functions and exceptions (e.g., `print`, `Exception`).
    - **Global namespace**: Created when a module is loaded; contains names defined at the module level.
    - **Enclosing namespace**: Exists in nested functions; refers to the namespace of the enclosing function.
    - **Local namespace**: Created inside a function; contains names defined within that function.
- The **LEGB rule** determines the order in which Python looks up names: Local → Enclosing → Global → Built-in.
- Each module has its own global namespace, so variables in different modules do not interfere.
- Namespaces are implemented as dictionaries mapping names to objects.
- You can inspect namespaces using built-in functions:
    - `globals()` returns the global namespace dictionary.
    - `locals()` returns the local namespace dictionary.
- Example:
    ```python
    x = 5  # global namespace

    def foo():
        y = 10  # local namespace
        print(locals())  # {'y': 10}
    ```
- Namespaces are dynamic; they are created at runtime and can change as the program executes.
- Proper use of namespaces improves code readability, maintainability, and reduces bugs due to name clashes.
- When importing modules, their global namespace is accessible via the module name (e.g., `math.sqrt`).
- Avoid polluting the global namespace by limiting the use of `from module import *`.
- Understanding namespaces is essential for working with modules, packages, and larger codebases.

```
```


## Notes on Importing Modules and Module Attributes

- **Importing modules** allows you to reuse code and organize functionality across multiple files.
- The basic import syntax is `import module_name`, which loads the entire module and makes its attributes accessible via `module_name.attribute`.
    ```python
    import math
    print(math.pi)
    ```
- To import specific attributes (functions, classes, variables) from a module, use `from module_name import attribute`.
    ```python
    from math import sqrt
    print(sqrt(16))
    ```
- You can import multiple attributes at once:
    ```python
    from math import sin, cos, tan
    ```
- Use the `as` keyword to create an alias for a module or attribute, which can make code more readable or avoid naming conflicts.
    ```python
    import numpy as np
    from math import sqrt as square_root
    ```
- Importing all attributes using `from module_name import *` is possible but discouraged, as it can pollute the namespace and cause conflicts.
- When a module is imported, Python executes its code and creates a namespace for it.
- Modules are only loaded once per interpreter session; subsequent imports use the cached version.
- You can reload a module using `importlib.reload(module)` if needed.
- Module attributes can include functions, classes, variables, and even other modules.
- Use relative imports (e.g., `from . import sibling_module`) within packages to refer to modules in the same package.
- Absolute imports specify the full path from the project's root package.
- The `__init__.py` file in a package can control what is imported when using `from package import *` by defining the `__all__` list.
- Import errors can occur if the module is not found or if there are circular dependencies; structure your code to avoid these issues.
- Good import practices improve code clarity, maintainability, and modularity.

```
```

## Notes on Module Hierarchy

- **Module hierarchy** refers to the organization of modules within packages and subpackages, creating a structured and scalable codebase.
- A **package** is a directory containing an `__init__.py` file and one or more module files (`.py`). Subpackages are nested directories with their own `__init__.py`.
- Hierarchical organization allows logical grouping of related modules, making code easier to navigate and maintain.
- Example structure:
    ```
    project/
        __init__.py
        module_a.py
        module_b.py
        utils/
            __init__.py
            helper.py
        data/
            __init__.py
            loader.py
            parser.py
    ```
- Modules within packages are imported using dot notation:
    ```python
    import project.module_a
    from project.utils import helper
    from project.data.parser import parse_data
    ```
- The `__init__.py` file can initialize the package, set up imports, or define the public API via `__all__`.
- Relative imports (using `.` and `..`) allow modules to import siblings or parent modules within the same package:
    ```python
    from .helper import some_function
    from ..data import loader
    ```
- Hierarchical module structures help avoid naming conflicts and support code reuse.
- Large projects often use multiple levels of packages and subpackages to separate concerns (e.g., models, views, controllers).
- Python's import system searches for modules/packages in the directories listed in `sys.path`.
- Properly structured module hierarchy improves scalability, testability, and collaboration in team environments.
- When distributing packages, use a clear hierarchy and include an appropriate `__init__.py` in each package/subpackage.

```
```

## Example: Content and Usage of Modules in a Hierarchical Package

### Directory Structure
```
project/
    __init__.py
    module_a.py
    module_b.py
    utils/
        __init__.py
        helper.py
    data/
        __init__.py
        loader.py
        parser.py
```

### File Contents

#### `project/__init__.py`
```python
# Initializes the 'project' package
__all__ = ['module_a', 'module_b', 'utils', 'data']
```

#### `project/module_a.py`
```python
def func_a():
    return "Function A from module_a"
```

#### `project/module_b.py`
```python
from .module_a import func_a  # Sibling import

def func_b():
    return f"Function B and {func_a()}"
```

#### `project/utils/__init__.py`
```python
# Initializes the 'utils' subpackage
__all__ = ['helper']
```

#### `project/utils/helper.py`
```python
def helper_func():
    return "Helper function from utils.helper"
```

#### `project/data/__init__.py`
```python
# Initializes the 'data' subpackage
__all__ = ['loader', 'parser']
```

#### `project/data/loader.py`
```python
from .parser import parse_data  # Sibling import

def load_data():
    data = "raw data"
    return parse_data(data)
```

#### `project/data/parser.py`
```python
def parse_data(data):
    return f"Parsed: {data}"
```

### Usage Examples

#### Importing Outside the Package
```python
# Outside 'project', e.g., in main.py
from project.module_a import func_a
from project.utils.helper import helper_func
from project.data.loader import load_data

print(func_a())         # Output: Function A from module_a
print(helper_func())    # Output: Helper function from utils.helper
print(load_data())      # Output: Parsed: raw data
```

#### Sibling Imports
- In `module_b.py`, `from .module_a import func_a` imports a sibling module within the same package.
- In `loader.py`, `from .parser import parse_data` imports a sibling module within the same subpackage.

#### Parent Imports
- To import from a parent package (e.g., from `data/loader.py` to `project/module_a.py`):
    ```python
    from ..module_a import func_a
    ```

### Notes
- Use relative imports (`.` for sibling, `..` for parent) within packages for maintainability.
- Absolute imports (`project.module_a`) are used outside the package or for clarity.
- Each module can be tested independently and imported as needed.
- Proper structure supports code reuse and avoids naming conflicts.


```
```

## Modular Development – Modules & Packages: Cheatsheet

### Creating Modules
- Write code in `.py` files to create modules.
- Import modules using `import module_name`.
- Use descriptive names and docstrings.
- Group related code for maintainability.

### Variable Scope
- Python uses the LEGB rule: Local, Enclosing, Global, Built-in.
- `global` modifies global variables; `nonlocal` modifies enclosing scope variables.
- Prefer passing data via parameters/returns over globals.

### Namespaces
- Containers mapping names to objects; types: built-in, global, enclosing, local.
- Each module has its own namespace.
- Inspect with `globals()` and `locals()`.
- Avoid polluting global namespace.

### Importing Modules & Attributes
- `import module`, `from module import attribute`, `import module as alias`.
- Avoid `from module import *` to prevent conflicts.
- Use relative imports within packages.
- Modules load once per session; reload with `importlib.reload()`.

### Module Hierarchy
- Organize modules in packages/subpackages with `__init__.py`.
- Import using dot notation: `package.module`.
- Use relative imports (`.`/`..`) for siblings/parents.
- Structure improves scalability and maintainability.

