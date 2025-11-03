## File Handling Basics

File handling allows programs to interact with files stored on disk. It is essential for reading data from files, writing output, and managing persistent information. Most programming languages provide built-in functions or libraries for file operations.

### Common File Operations

#### 1. Opening Files (`open`)
- The `open` function is used to access a file.
- Syntax (Python example):  
    ```python
    file = open('filename.txt', 'mode')
    ```
- Modes include:
    - `'r'`: Read (default)
    - `'w'`: Write (creates/truncates file)
    - `'a'`: Append (writes at end)
    - `'b'`: Binary mode (e.g., `'rb'`, `'wb'`)
    - `'x'`: Create (fails if file exists)
- Always close files after use with `file.close()` or use context managers (`with open(...) as file:`).

#### 2. Reading Files (`read`)
- Read entire file:  
    ```python
    content = file.read()
    ```
- Read line by line:  
    ```python
    line = file.readline()
    lines = file.readlines()
    ```
- For large files, iterate:
    ```python
    for line in file:
            process(line)
    ```

#### 3. Writing to Files (`write`)
- Write text to file:
    ```python
    file.write('Hello World')
    ```
- Write multiple lines:
    ```python
    file.writelines(['Line1\n', 'Line2\n'])
    ```
- Writing in binary mode requires bytes:
    ```python
    file.write(b'binary data')
    ```

#### 4. Other Operations
- **Closing Files:**  
    Always close files to free resources:
    ```python
    file.close()
    ```
- **Checking File Existence:**  
    Use libraries like `os.path.exists('filename.txt')`.
- **Deleting Files:**  
    Use `os.remove('filename.txt')`.
- **Renaming Files:**  
    Use `os.rename('old.txt', 'new.txt')`.
- **Seeking:**  
    Move file pointer with `file.seek(offset)`.

### Best Practices
- Use context managers (`with open(...) as file:`) for automatic closing.
- Handle exceptions (e.g., `try...except`) for robust code.
- Always specify correct mode for intended operation.
- Avoid hardcoding file paths; use variables or configuration.


```
```

### File Handling Cheatsheet

- **Opening Files:**  
    `open('filename', 'mode')`  
    Modes: `'r'`, `'w'`, `'a'`, `'b'`, `'x'`

- **Reading Files:**  
    `file.read()`, `file.readline()`, `file.readlines()`  
    Iterate: `for line in file:`

- **Writing Files:**  
    `file.write('text')`, `file.writelines([...])`  
    Binary: `file.write(b'data')`

- **Other Operations:**  
    Close: `file.close()`  
    Context manager: `with open(...) as file:`  
    Check existence: `os.path.exists()`  
    Delete: `os.remove()`  
    Rename: `os.rename()`  
    Seek: `file.seek(offset)`

- **Best Practices:**  
    Use context managers, handle exceptions, specify correct mode, avoid hardcoded paths.