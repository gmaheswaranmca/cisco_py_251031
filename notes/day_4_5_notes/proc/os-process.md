# ⚡ 1. `os` Module – Basic Process Automation

The `os` module lets you interact with the **environment and filesystem**, and start simple processes.

### Example: Run a System Command

```python
import os

# Run a system command
exit_code = os.system("echo Hello from OS module")
print("Exit code:", exit_code)
```

👉 Drawback: `os.system()` just runs the command—it doesn’t capture the output.
That’s where **`subprocess`** is better.

---

### Example: File & Directory Automation

```python
import os

# Current working directory
print("Current directory:", os.getcwd())

# List files
print("Files:", os.listdir("."))

# Create a new folder
os.mkdir("test_folder")

# Rename a file/folder
os.rename("test_folder", "renamed_folder")

# Remove directory
os.rmdir("renamed_folder")
```

---

# ⚡ 2. `subprocess` Module – Advanced Process Automation

The `subprocess` module is the **recommended way** to spawn new processes, connect to input/output/error pipes, and get results.

### Example: Running a Command and Capturing Output

```python
import subprocess

result = subprocess.run(["echo", "Hello from subprocess"], capture_output=True, text=True)
print("Output:", result.stdout)
print("Exit code:", result.returncode)
```

---

### Example: Run `ls` (Linux/macOS) or `dir` (Windows)

```python
import subprocess
import platform

if platform.system() == "Windows":
    cmd = ["cmd", "/c", "dir"]
else:
    cmd = ["ls", "-l"]

result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)
```

---

### Example: Run a Background Process

```python
import subprocess

# Open Notepad (Windows) or gedit (Linux) in background
p = subprocess.Popen(["notepad.exe"])  # For Windows
# p = subprocess.Popen(["gedit"])      # For Linux
print("Started process with PID:", p.pid)
```

---

### Example: Pipeline (like `ls | grep py`)

```python
import subprocess

p1 = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "py"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)

output, _ = p2.communicate()
print("Python files:\n", output)
```

---

# ⚡ 3. Combining `os` and `subprocess` for Automation

You can use `os` for filesystem navigation and `subprocess` for running commands.

### Example: Automating a Deployment Step

```python
import os
import subprocess

# Navigate to project folder
os.chdir("/path/to/project")

# Pull latest code
subprocess.run(["git", "pull"])

# Run build script
subprocess.run(["python", "build.py"])

# Start server
subprocess.Popen(["python", "app.py"])
```

---

# ✅ Summary

* Use **`os`** for environment, paths, files, directories.
* Use **`subprocess`** for running commands, capturing output, and automating shell pipelines.
* Together, they let you build **end-to-end automation scripts** for DevOps, deployment, testing, etc.


```
```
# dive **deep into the `os` module** for **process automation**.
While `subprocess` is used for running external processes, the `os` module is mainly about **interacting with the operating system** — managing files, directories, environment variables, and simple process controls.

---

# 🔑 **Key Areas of Process Automation with `os`**

---

## 1. **Process Management**

The `os` module allows you to **start processes**, check **process IDs**, and even **terminate processes**.

```python
import os

# Get current process ID
print("Current PID:", os.getpid())

# Get parent process ID
print("Parent PID:", os.getppid())
```

You can also **launch a new process**:

```python
os.system("notepad")   # Windows
# os.system("gedit")   # Linux
```

But remember: `os.system()` just runs the command — it doesn’t capture output. For advanced process management, `subprocess` is better.

---

## 2. **Working with Directories**

Process automation often requires moving around directories.

```python
import os

# Current working directory
print("CWD:", os.getcwd())

# Change working directory
os.chdir("C:/Windows")
print("Changed to:", os.getcwd())

# List contents
print("Files:", os.listdir("."))
```

---

## 3. **Creating, Renaming, Removing**

You can **automate directory and file management**.

```python
# Make a directory
os.mkdir("new_folder")

# Rename it
os.rename("new_folder", "renamed_folder")

# Remove it
os.rmdir("renamed_folder")
```

For **recursive deletes** (folders with files inside), use `shutil.rmtree()`.

---

## 4. **Environment Variables**

Processes depend on environment variables (`PATH`, `HOME`, etc.).
You can **read, set, and delete** them with `os.environ`.

```python
import os

# Read environment variables
print("PATH:", os.environ["PATH"])

# Set a new variable
os.environ["MY_VAR"] = "HelloOS"
print("MY_VAR:", os.environ.get("MY_VAR"))

# Delete a variable
del os.environ["MY_VAR"]
```

---

## 5. **File Information & Permissions**

Automation often requires checking file metadata or changing access.

```python
import os

# File stats
info = os.stat("test.txt")
print("Size:", info.st_size, "bytes")

# Change file mode (permissions)
os.chmod("test.txt", 0o777)  # rwxrwxrwx
```

---

## 6. **Path Handling**

`os.path` helps automate cross-platform file handling.

```python
import os

file_path = "/home/user/file.txt"

print("Exists:", os.path.exists(file_path))
print("Is File:", os.path.isfile(file_path))
print("Is Dir:", os.path.isdir(file_path))
print("Absolute Path:", os.path.abspath(file_path))
print("Join Path:", os.path.join("/home", "user", "docs", "a.txt"))
```

---

## 7. **Process Spawning (`fork`/`exec`)**

On **Unix/Linux**, you can spawn processes with `os.fork()` (not available on Windows).

```python
import os

pid = os.fork()
if pid == 0:
    # Child process
    print("Child process PID:", os.getpid())
else:
    # Parent process
    print("Parent process PID:", os.getpid())
```

For replacing a process:

```python
os.execlp("ls", "ls", "-l")  # replaces current process with `ls -l`
```

---

## 8. **Automation Example – Mini Backup Script**

Using only `os`:

```python
import os
import time
import shutil

def backup_folder(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = os.path.join(dest, backup_name)

    shutil.copytree(src, backup_path)
    print(f"Backup created at {backup_path}")

# Usage
backup_folder("my_project", "backups")
```

---

# ✅ Summary

The `os` module enables **process automation by controlling the environment and filesystem**:

* Manage **process IDs** and run commands (`os.system`, `os.fork`, `os.exec`).
* Work with **directories and files** (`os.chdir`, `os.mkdir`, `os.remove`).
* Automate using **environment variables** (`os.environ`).
* Handle **permissions and metadata** (`os.chmod`, `os.stat`).
* Cross-platform **path automation** (`os.path`).

```
```

# list of **real-world automation project problem statements** that can be solved using only **`os`** and/or **`subprocess`** in Python:

---

## 🔹 **File & Directory Automation**

1. **Daily Backup Automation**
   Automate copying a project folder into a timestamped backup folder every day.
2. **Log Rotation Script**
   Move old log files into an archive folder and compress them once they exceed a certain size.
3. **Duplicate File Finder**
   Scan a directory tree and detect duplicate files by name/size, then list or delete them.
4. **Automatic File Organizer**
   Organize files in a downloads folder into subfolders (Images, Documents, Videos) based on file extension.
5. **Large File Cleaner**
   Find files larger than a given size and move them to a cleanup folder for review.

---

## 🔹 **System & Process Management**

6. **System Resource Monitor**
   Automate running system commands (`top`, `tasklist`, `df -h`) and log CPU/memory/disk usage.
7. **Process Killer Script**
   Search for a process by name (e.g., "chrome") and terminate it automatically.
8. **Startup Script Manager**
   Create a script that launches a set of applications automatically at system startup.
9. **Scheduled Job Runner**
   Run a Python script (or other command) at fixed intervals, simulating cron/scheduler.
10. **Service Health Checker**
    Periodically check if a process (e.g., `nginx`, `mysql`) is running, restart it if not.

---

## 🔹 **Networking & Deployment**

11. **Automated Ping Sweep**
    Ping a range of IP addresses to find active devices on a network.
12. **Remote File Transfer Automation**
    Automate copying files to/from a server using `scp` or `ftp` commands.
13. **Simple Deployment Script**
    Navigate to a project folder, pull latest code from Git, run build commands, and restart a server.
14. **Website Uptime Monitor**
    Use `curl` or `ping` via `subprocess` to check if a website is up, log downtime.
15. **Firewall Rule Updater**
    Automate adding/removing firewall rules by executing system commands.

---

## 🔹 **System Maintenance**

16. **Disk Cleanup Automation**
    Automatically remove temp files, cache, or old backups beyond X days.
17. **Auto Software Installer**
    Run OS-level package manager commands (`apt-get`, `yum`, `choco`, `brew`) from Python to install/update software.
18. **Patch Update Script**
    Automate updating system packages and saving update logs.
19. **Printer Queue Cleaner**
    Detect stuck print jobs and clear them automatically.
20. **Automated Screenshot & Report**
    Use OS utilities to capture a screenshot at intervals and store them for monitoring.

```
```

# **5 real-world automation projects** using `os` and/or `subprocess` into **mini-project statements with objectives & expected outcomes**.

---

## **1. Daily Backup Automation**

**Problem Statement:**
Automate daily backups of a project directory into a timestamped folder to ensure data safety.

**Objectives:**

* Detect the target project directory.
* Create a backup folder with the current date and time in its name.
* Copy all files and subdirectories into the backup location.

**Expected Outcomes:**

* A backup folder is created daily without manual intervention.
* Old versions are preserved with unique timestamps.
* User receives confirmation (print/log).

---

## **2. Process Killer Script**

**Problem Statement:**
Kill unnecessary processes (e.g., Chrome, VSCode) automatically to free system resources.

**Objectives:**

* Search for running processes by name.
* Terminate the matching process IDs.
* Optionally log the action with process details.

**Expected Outcomes:**

* Targeted processes are killed instantly.
* System resources are freed up.
* Script prevents accidental kills by confirming with user/logging.

---

## **3. Automated Ping Sweep (Network Scanner)**

**Problem Statement:**
Scan a local network (e.g., `192.168.1.1–192.168.1.254`) to identify active devices.

**Objectives:**

* Loop through a range of IPs.
* Execute system `ping` command for each IP.
* Collect results and save active IPs into a log file.

**Expected Outcomes:**

* A report listing all live devices in the network.
* Helps identify new/unauthorized devices.
* Works across Windows/Linux with OS commands.

---

## **4. Disk Cleanup Automation**

**Problem Statement:**
Automate the cleanup of temporary files, cache, and logs older than a specific number of days.

**Objectives:**

* Identify temporary directories (e.g., `/tmp`, `%TEMP%`).
* Find and delete files older than N days.
* Log deleted files for review.

**Expected Outcomes:**

* Reduces disk usage by clearing old files.
* Keeps only recent logs/cache.
* Automated scheduling possible (cron/Task Scheduler).

---

## **5. Simple Deployment Script**

**Problem Statement:**
Automate deployment steps for a web project (e.g., pulling latest code, installing dependencies, restarting server).

**Objectives:**

* Navigate to project directory.
* Run `git pull` to fetch latest changes.
* Install dependencies (`pip install -r requirements.txt` / `npm install`).
* Restart the web server process.

**Expected Outcomes:**

* Deployment completed in one command/script.
* Reduced manual errors in deployment.
* Saves developer time in repetitive tasks.
