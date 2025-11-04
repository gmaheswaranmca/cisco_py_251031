# **File & Directory Management CLI Tool**

### **Problem Statement**

Build a command-line tool in Python that automates common file and directory operations like creating, renaming, deleting, moving, and listing files.

---

### **Objectives**

* Allow users to execute **basic shell commands** (like `mkdir`, `ls`, `rm`, `mv`, `cp`) from Python.
* Provide cross-platform support (Windows/Linux/Mac).
* Handle errors (e.g., file not found, permission denied).
* Log all operations for audit purposes.

---

### **Features**

1. **Create a Directory** → `python file_tool.py mkdir myfolder`
2. **List Files/Dirs** → `python file_tool.py ls myfolder`
3. **Rename File/Dir** → `python file_tool.py rename old.txt new.txt`
4. **Copy File/Dir** → `python file_tool.py cp file.txt backup/`
5. **Move File/Dir** → `python file_tool.py mv file.txt archive/`
6. **Delete File/Dir** → `python file_tool.py rm oldfolder/`
7. **Show Current Working Directory** → `python file_tool.py pwd`

---

### **Expected Outcomes**

* A single Python script that acts like a **mini shell** for file/directory commands.
* Reduces dependency on OS terminal by wrapping commands in Python.
* Logs all executed commands with success/failure status.

---

👉 This project will give you practice in:

* `os` module (`os.getcwd`, `os.listdir`, `os.rename`, `os.remove`, `os.makedirs`, `os.rmdir`, etc.)
* `subprocess` for executing actual OS commands (`ls`, `dir`, `rm`, etc.).
* Error handling (`try-except` with `OSError`).
* Argument parsing (`argparse` module).

```
```

you’ll have both:

1. **Safe Python wrappers** (`os`, `shutil`).
2. **Direct shell execution** (`subprocess`).

---

## 📌 Updated Code (with `subprocess` support)

```python
import os
import shutil
import argparse
import subprocess

def list_dir(path="."):
    try:
        items = os.listdir(path)
        print(f"Contents of {path}:")
        for item in items:
            print(" -", item)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found")

def make_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")
    except Exception as e:
        print(f"Error creating directory: {e}")

def remove(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Directory removed: {path}")
        elif os.path.isfile(path):
            os.remove(path)
            print(f"File removed: {path}")
        else:
            print(f"Error: '{path}' does not exist")
    except Exception as e:
        print(f"Error removing {path}: {e}")

def rename(src, dst):
    try:
        os.rename(src, dst)
        print(f"Renamed '{src}' → '{dst}'")
    except Exception as e:
        print(f"Error renaming: {e}")

def copy(src, dst):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy(src, dst)
        print(f"Copied '{src}' → '{dst}'")
    except Exception as e:
        print(f"Error copying: {e}")

def move(src, dst):
    try:
        shutil.move(src, dst)
        print(f"Moved '{src}' → '{dst}'")
    except Exception as e:
        print(f"Error moving: {e}")

def show_pwd():
    print("Current Directory:", os.getcwd())

def run_command(cmd):
    """Run raw OS command using subprocess"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            print("Error:", result.stderr.strip())
    except Exception as e:
        print(f"Error running command: {e}")

def main():
    parser = argparse.ArgumentParser(description="File & Directory Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # mkdir
    parser_mkdir = subparsers.add_parser("mkdir", help="Create a directory")
    parser_mkdir.add_argument("path")

    # ls
    parser_ls = subparsers.add_parser("ls", help="List directory contents")
    parser_ls.add_argument("path", nargs="?", default=".")

    # rm
    parser_rm = subparsers.add_parser("rm", help="Remove file or directory")
    parser_rm.add_argument("path")

    # rename
    parser_rename = subparsers.add_parser("rename", help="Rename file/directory")
    parser_rename.add_argument("src")
    parser_rename.add_argument("dst")

    # cp
    parser_cp = subparsers.add_parser("cp", help="Copy file or directory")
    parser_cp.add_argument("src")
    parser_cp.add_argument("dst")

    # mv
    parser_mv = subparsers.add_parser("mv", help="Move file or directory")
    parser_mv.add_argument("src")
    parser_mv.add_argument("dst")

    # pwd
    subparsers.add_parser("pwd", help="Show current working directory")

    # exec (new feature: raw commands)
    parser_exec = subparsers.add_parser("exec", help="Run raw OS command")
    parser_exec.add_argument("cmd", nargs=argparse.REMAINDER, help="Command to execute")

    args = parser.parse_args()

    if args.command == "mkdir":
        make_dir(args.path)
    elif args.command == "ls":
        list_dir(args.path)
    elif args.command == "rm":
        remove(args.path)
    elif args.command == "rename":
        rename(args.src, args.dst)
    elif args.command == "cp":
        copy(args.src, args.dst)
    elif args.command == "mv":
        move(args.src, args.dst)
    elif args.command == "pwd":
        show_pwd()
    elif args.command == "exec":
        run_command(" ".join(args.cmd))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

---

## 🔹 Example Usage

### ✅ Python-safe operations

```bash
python file_tool.py mkdir myfolder
python file_tool.py ls
python file_tool.py rename myfolder newfolder
python file_tool.py cp newfolder backup_folder
python file_tool.py rm backup_folder
```

### ✅ Run raw system commands (via subprocess)

```bash
python file_tool.py exec ls -l
python file_tool.py exec dir         # Windows
python file_tool.py exec echo Hello World
python file_tool.py exec ping google.com -c 2   # Linux/Mac
python file_tool.py exec tasklist    # Windows process list
```

---

⚡ This way, you get **both safety (`os`)** and **power (`subprocess`)** in one tool.

