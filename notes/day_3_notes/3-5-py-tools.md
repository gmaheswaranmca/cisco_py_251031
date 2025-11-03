## Unit Testing – `unittest` & `pytest`

### What is Unit Testing?
Unit testing is the process of testing individual units of code (functions, methods, classes) to ensure they work as expected. It helps catch bugs early and supports code refactoring.

---

### `unittest` Module

- **Standard Library**: Built-in Python module for unit testing.
- **Structure**: Tests are organized in classes derived from `unittest.TestCase`.
- **Assertions**: Provides methods like `assertEqual`, `assertTrue`, `assertRaises`, etc.
- **Test Discovery**: Can automatically discover tests in files named `test*.py`.

**Example:**
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

**Running Tests:**
```bash
python test_file.py
```

---

### `pytest` Framework

- **Third-party**: Needs installation (`pip install pytest`).
- **Simplicity**: Tests are simple functions, no need for classes.
- **Powerful Features**: Rich assertions, fixtures, parameterization, plugins.
- **Test Discovery**: Finds tests in files named `test_*.py` or `*_test.py`.

**Example:**
```python
def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2
```

**Running Tests:**
```bash
pytest
```

---

### Comparison

| Feature         | unittest           | pytest              |
|-----------------|-------------------|---------------------|
| Built-in        | Yes               | No                  |
| Test Structure  | Classes           | Functions/Classes   |
| Fixtures        | Basic             | Advanced            |
| Plugins         | Limited           | Extensive           |
| Assertions      | Methods           | Python `assert`     |

---

### Best Practices

- Name test files and functions clearly.
- Use setup/teardown methods or fixtures for reusable test code.
- Run tests frequently during development.
- Integrate with CI/CD for automated testing.

---

### Resources

- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Python Testing Tools](https://wiki.python.org/moin/PythonTestingTools)

```
```


## Debugger

### What is a Debugger?
A debugger is a tool that helps developers inspect, control, and modify the execution of code to identify and fix bugs. It allows you to pause execution, examine variables, step through code, and set breakpoints.

---

### Python Debugging Tools

#### 1. `pdb` (Python Debugger)

- **Standard Library**: Comes with Python.
- **Features**: Interactive command-line debugging, breakpoints, stepping, inspecting variables.
- **Usage**: Insert `import pdb; pdb.set_trace()` in your code or run scripts with `python -m pdb script.py`.

**Common Commands:**
| Command | Description                |
|---------|----------------------------|
| `l`     | List source code           |
| `n`     | Next line                  |
| `s`     | Step into function         |
| `c`     | Continue execution         |
| `b`     | Set breakpoint             |
| `p`     | Print variable             |
| `q`     | Quit debugger              |

**Example:**
```python
def divide(a, b):
    import pdb; pdb.set_trace()
    return a / b

result = divide(10, 2)
```

---

#### 2. IDE Debuggers

- **Popular IDEs**: VS Code, PyCharm, Thonny, etc.
- **Features**: Graphical interface, breakpoints, variable inspection, call stack navigation, conditional breakpoints.
- **Usage**: Set breakpoints by clicking next to line numbers, use debug controls to step through code.

---

#### 3. Remote Debugging

- **Purpose**: Debug code running on remote servers or containers.
- **Tools**: `debugpy` (for VS Code), PyCharm remote debugger.
- **Setup**: Install and configure remote debugging tools, connect IDE to remote process.

---

### Best Practices

- Use breakpoints to isolate problematic code.
- Inspect variable values and program state during execution.
- Step through code to understand flow and logic.
- Remove or disable debugging statements before deploying code.

---

### Resources

- [pdb documentation](https://docs.python.org/3/library/pdb.html)
- [Debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)
- [PyCharm Debugger Guide](https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html)


```
```



## PyDoc

### What is PyDoc?
PyDoc is a documentation generator for Python modules. It extracts docstrings from Python code and presents them as formatted documentation, either in text, HTML, or via a local web server.

---

### Features

- **Automatic Documentation**: Generates documentation from docstrings in modules, classes, functions, and methods.
- **Multiple Formats**: Outputs documentation as plain text, HTML, or serves it via a web interface.
- **Standard Library Tool**: Included with Python, no installation required.

---

### Usage

#### 1. Command Line

- **View Documentation in Console**:
    ```bash
    pydoc <module_name>
    ```
    Example:
    ```bash
    pydoc math
    ```

- **Generate HTML Documentation**:
    ```bash
    pydoc -w <module_name>
    ```
    This creates an HTML file for the specified module.

- **Start Local Documentation Server**:
    ```bash
    pydoc -p 8080
    ```
    Opens a web server at `http://localhost:8080` to browse documentation interactively.

---

### Writing Good Docstrings

- Use triple quotes (`"""docstring"""`) for module, class, and function documentation.
- Describe purpose, parameters, return values, and exceptions.
- Example:
    ```python
    def add(a, b):
            """
            Adds two numbers.

            Args:
                    a (int): First number.
                    b (int): Second number.

            Returns:
                    int: The sum of a and b.
            """
            return a + b
    ```

---

### Best Practices

- Document all public modules, classes, and functions.
- Keep docstrings concise but informative.
- Follow [PEP 257](https://peps.python.org/pep-0257/) conventions for docstrings.

---

### Resources

- [PyDoc documentation](https://docs.python.org/3/library/pydoc.html)
- [PEP 257 – Docstring conventions](https://peps.python.org/pep-0257/)
- [Documenting Python Code](https://realpython.com/documenting-python-code/)


```
```



## Installing Python Modules

### What are Python Modules?
Python modules are reusable pieces of code, typically distributed as packages, that add functionality to your projects. Modules can be installed from the Python Package Index (PyPI) or other sources.

---

### Installing Modules with `pip`

- **pip**: The standard package manager for Python.
- **Basic Installation**:
    ```bash
    pip install <package_name>
    ```
    Example:
    ```bash
    pip install requests
    ```

- **Installing Specific Versions**:
    ```bash
    pip install <package_name>==<version>
    ```
    Example:
    ```bash
    pip install numpy==1.24.0
    ```

- **Upgrading Packages**:
    ```bash
    pip install --upgrade <package_name>
    ```

- **Installing from a Requirements File**:
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file lists all dependencies for a project.

---

### Other Installation Methods

- **From Source**:
    ```bash
    pip install git+https://github.com/user/repo.git
    ```
- **Using `setup.py`**:
    ```bash
    python setup.py install
    ```
    (Mostly for legacy projects.)

---

### Managing Installed Packages

- **List Installed Packages**:
    ```bash
    pip list
    ```
- **Show Package Info**:
    ```bash
    pip show <package_name>
    ```
- **Uninstall a Package**:
    ```bash
    pip uninstall <package_name>
    ```

---

### Best Practices

- Use virtual environments to isolate project dependencies.
- Pin package versions in `requirements.txt` for reproducibility.
- Regularly update packages to get security and bug fixes.

---

### Troubleshooting

- If you encounter permission errors, use `pip install --user <package_name>`.
- For system-wide installations, you may need `sudo` (Linux/macOS).
- Ensure `pip` matches your Python version (`pip3` for Python 3).

---

### Resources

- [pip documentation](https://pip.pypa.io/en/stable/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [PyPI – Python Package Index](https://pypi.org/)

```
```



## Distributing Python Modules

### Why Distribute Modules?
Distributing Python modules allows you to share your code with others, reuse it across projects, and publish it to repositories like PyPI for public or private use.

---

### Packaging Your Module

#### 1. Project Structure

Organize your project directory:
```
your_package/
├── your_package/
│   └── __init__.py
├── tests/
├── README.md
├── setup.py
├── pyproject.toml
├── LICENSE
```

#### 2. Metadata Files

- **`setup.py`**: Traditional build script (being replaced by `pyproject.toml`).
- **`pyproject.toml`**: Modern standard for build configuration and dependencies.

Example `pyproject.toml`:
```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "your_package"
version = "0.1.0"
description = "A sample Python package"
authors = [{name = "Your Name", email = "you@example.com"}]
```

---

### Building Distributions

- **Source Distribution**:
    ```bash
    python -m build
    ```
    Creates `.tar.gz` and `.whl` files in the `dist/` directory.

- **Legacy Method**:
    ```bash
    python setup.py sdist bdist_wheel
    ```

---

### Publishing to PyPI

1. **Register on PyPI**: [https://pypi.org/account/register/](https://pypi.org/account/register/)
2. **Install Twine**:
    ```bash
    pip install twine
    ```
3. **Upload Package**:
    ```bash
    twine upload dist/*
    ```

For test uploads, use [TestPyPI](https://test.pypi.org/):
```bash
twine upload --repository testpypi dist/*
```

---

### Versioning and Documentation

- Follow [Semantic Versioning](https://semver.org/) for releases.
- Include a clear `README.md` and license.
- Document installation and usage instructions.

---

### Best Practices

- Test your package before distribution.
- Use `.gitignore` to exclude unnecessary files.
- Keep dependencies minimal and specify them in metadata.

---

### Resources

- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [PyPI documentation](https://pypi.org/help/)
- [setuptools documentation](https://setuptools.pypa.io/en/latest/)

```
```



## Virtual Environment

### What is a Virtual Environment?
A virtual environment is an isolated workspace for Python projects. It allows you to manage dependencies separately for each project, avoiding conflicts between packages and versions.

---

### Why Use Virtual Environments?

- Prevents dependency clashes between projects.
- Keeps global Python installation clean.
- Makes projects reproducible and easier to share.

---

### Creating a Virtual Environment

#### Using `venv` (Standard Library)

- **Create a virtual environment**:
    ```bash
    python -m venv venv_name
    ```
    Example:
    ```bash
    python -m venv myenv
    ```

- **Activate the environment**:
    - **Windows**:
        ```bash
        myenv\Scripts\activate
        ```
    - **macOS/Linux**:
        ```bash
        source myenv/bin/activate
        ```

- **Deactivate**:
    ```bash
    deactivate
    ```

#### Using `virtualenv` (Third-party)

- **Install**:
    ```bash
    pip install virtualenv
    ```
- **Create**:
    ```bash
    virtualenv venv_name
    ```

---

### Managing Dependencies

- Install packages inside the activated environment using `pip`.
- Freeze dependencies to a file:
    ```bash
    pip freeze > requirements.txt
    ```
- Install dependencies from a file:
    ```bash
    pip install -r requirements.txt
    ```

---

### Best Practices

- Always use a virtual environment for new projects.
- Store `requirements.txt` in version control.
- Avoid installing packages globally unless necessary.

---

### Resources

- [venv documentation](https://docs.python.org/3/library/venv.html)
- [virtualenv documentation](https://virtualenv.pypa.io/en/latest/)
- [Python Packaging Guide: Virtual Environments](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments)


```
```


## Static Analysis – `pylint`

### What is Static Analysis?
Static analysis examines code without executing it, identifying potential errors, code smells, and style issues. It helps improve code quality, maintainability, and adherence to coding standards.

---

### What is `pylint`?

- **pylint** is a popular static analysis tool for Python.
- Checks for errors, enforces coding standards (PEP 8), detects unused code, and provides code metrics.
- Assigns a score to your code based on detected issues.

---

### Installing `pylint`

```bash
pip install pylint
```

---

### Using `pylint`

- **Analyze a Python file**:
    ```bash
    pylint your_script.py
    ```
- **Analyze a package or module**:
    ```bash
    pylint your_package/
    ```

---

### Output

- Lists warnings, errors, refactor suggestions, and convention violations.
- Provides a summary score (10/10 is perfect).

**Example Output:**
```
your_script.py:1:0: C0114: Missing module docstring (missing-module-docstring)
your_script.py:3:4: C0103: Variable name "x" doesn't conform to snake_case naming style (invalid-name)
------------------------------------------------------------------
Your code has been rated at 8.50/10
```

---

### Configuration

- Customize checks with a `.pylintrc` config file.
- Disable specific warnings:
    ```bash
    pylint --disable=C0114 your_script.py
    ```
- Integrate with IDEs for real-time feedback.

---

### Best Practices

- Run `pylint` regularly to catch issues early.
- Address critical errors and warnings.
- Use configuration files to tailor checks to your project.
- Combine with other tools (e.g., `flake8`, `mypy`) for comprehensive analysis.

---

### Resources

- [pylint documentation](https://pylint.pycqa.org/en/latest/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Static Analysis Tools for Python](https://wiki.python.org/moin/StaticAnalysis)

```
```


## Python Tools Cheatsheet

### Unit Testing (`unittest`, `pytest`)
- `unittest`: Built-in, class-based, uses assertions.
- `pytest`: Third-party, function-based, rich features, plugins.
- Run tests: `python -m unittest` or `pytest`.

### Debugger
- `pdb`: Built-in, command-line debugging (`import pdb; pdb.set_trace()`).
- IDEs: VS Code, PyCharm offer graphical debugging.
- Remote debugging: Use `debugpy`, PyCharm remote tools.

### PyDoc
- Generates documentation from docstrings.
- View docs: `pydoc <module>`, HTML: `pydoc -w <module>`, web server: `pydoc -p 8080`.
- Write clear docstrings, follow PEP 257.

### Installing Python Modules
- Use `pip install <package>`.
- Requirements file: `pip install -r requirements.txt`.
- Manage packages: `pip list`, `pip show`, `pip uninstall`.

### Distributing Python Modules
- Structure: `your_package/`, `setup.py`, `pyproject.toml`, `README.md`.
- Build: `python -m build`.
- Publish: `twine upload dist/*` to PyPI.

### Virtual Environment
- Create: `python -m venv myenv`.
- Activate: `myenv\Scripts\activate` (Windows), `source myenv/bin/activate` (macOS/Linux).
- Manage dependencies: `pip freeze > requirements.txt`.

### Static Analysis (`pylint`)
- Install: `pip install pylint`.
- Run: `pylint your_script.py`.
- Checks code quality, style, errors; configurable via `.pylintrc`.

---
**Tip:** Use these tools together for robust, maintainable Python projects.

