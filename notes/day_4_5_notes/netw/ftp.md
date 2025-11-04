# **FTP automation in Python**.

Unlike SCP/SSH, FTP is an **older, plain-text protocol** (port 21) often used for file transfer in legacy systems.
Python gives us tools to **connect, upload, download, list files, delete files, etc.**

---

## 🔑 Option 1: Using `ftplib` (Standard Library)

Python’s built-in `ftplib` is enough for most FTP automation.

### Example: Upload, Download, and List Files

```python
from ftplib import FTP

def ftp_automation(host, username, password, local_file, remote_file):
    try:
        # Connect to FTP Server
        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        print("Connected:", ftp.getwelcome())

        # Upload file
        with open(local_file, "rb") as f:
            ftp.storbinary(f"STOR {remote_file}", f)
        print(f"Uploaded {local_file} → {remote_file}")

        # List files in current directory
        print("Files on server:")
        ftp.retrlines("LIST")

        # Download the same file
        with open("downloaded_copy.txt", "wb") as f:
            ftp.retrbinary(f"RETR {remote_file}", f.write)
        print(f"Downloaded {remote_file} → downloaded_copy.txt")

        # Close connection
        ftp.quit()
        return True

    except Exception as e:
        return f"Error: {e}"


# Usage
ftp_automation("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu", "test.txt", "remote_test.txt")
```

👉 Here I used the **public FTP test server**:

* Host: `ftp.dlptest.com`
* User: `dlpuser`
* Password: `rNrKYTX9g7z3RgJRmxWuGHbeu`

---

## 🔑 Option 2: Secure FTP (SFTP/FTPS)

Since FTP is insecure, you might want **encrypted alternatives**:

* **SFTP** → Use `paramiko` or `pysftp` (SSH-based).
* **FTPS** → Use `ftplib.FTP_TLS`.

### Example: FTPS with `FTP_TLS`

```python
from ftplib import FTP_TLS

def ftps_automation(host, username, password):
    try:
        ftps = FTP_TLS(host)
        ftps.login(user=username, passwd=password)
        ftps.prot_p()  # Secure data connection
        print("Connected securely:", ftps.getwelcome())

        print("Files on server:")
        ftps.retrlines("LIST")

        ftps.quit()
        return True
    except Exception as e:
        return f"Error: {e}"
```

---

## 🔑 Option 3: Using `subprocess` with System `ftp`

If you want to script around system-installed `ftp` command:

```python
import subprocess

def ftp_with_subprocess(host, username, password, local_file, remote_file):
    script = f"""
open {host}
user {username} {password}
put {local_file} {remote_file}
bye
"""
    try:
        result = subprocess.run(
            ["ftp", "-n"],
            input=script,
            text=True,
            capture_output=True
        )
        return result.stdout
    except Exception as e:
        return f"Error: {e}"
```

---

## ✅ Summary

* Use **`ftplib`** if you just need plain FTP automation (upload, download, list).
* Use **`FTP_TLS`** for **FTPS (encrypted FTP over SSL/TLS)**.
* Use **SFTP (paramiko/pysftp)** if you want **secure file transfers via SSH**.
* Use **`subprocess`** if you want to control system `ftp` command directly.
