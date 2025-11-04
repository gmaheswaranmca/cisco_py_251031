# to **SCP automation in Python**.
SCP (**Secure Copy Protocol**) is built on top of SSH and is used to transfer files securely between local and remote systems.

There are a couple of ways to do this in Python:

---

## 🔑 Option 1: Using **Paramiko + scp module**

Paramiko handles SSH, and the `scp` package wraps it for file transfer.

### Install:

```bash
pip install paramiko scp
```

### Example: Upload & Download File

```python
import paramiko
from scp import SCPClient

def scp_transfer(host, port, username, password, local_file, remote_path):
    try:
        # Setup SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)

        # SCP Client
        with SCPClient(ssh.get_transport()) as scp:
            # Upload
            scp.put(local_file, remote_path)
            print(f"Uploaded {local_file} → {remote_path}")

            # Download back (for testing)
            scp.get(remote_path, "downloaded_copy.txt")
            print(f"Downloaded {remote_path} → downloaded_copy.txt")

        ssh.close()
        return True

    except Exception as e:
        return f"Error: {e}"

# Usage
scp_transfer("192.168.1.10", 22, "ubuntu", "password123", "test.txt", "/home/ubuntu/test.txt")
```

---

## 🔑 Option 2: Using **Paramiko SFTP**

Paramiko also has **SFTP** support, which works similarly to SCP.

```python
import paramiko

def sftp_transfer(host, port, username, password, local_file, remote_path):
    try:
        # SSH setup
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)

        # SFTP client
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload
        sftp.put(local_file, remote_path)
        print(f"Uploaded {local_file} → {remote_path}")

        # Download back
        sftp.get(remote_path, "sftp_copy.txt")
        print(f"Downloaded {remote_path} → sftp_copy.txt")

        sftp.close()
        transport.close()
        return True

    except Exception as e:
        return f"Error: {e}"

# Usage
sftp_transfer("192.168.1.10", 22, "ubuntu", "password123", "test.txt", "/home/ubuntu/test.txt")
```

---

## 🔑 Option 3: Automating with `subprocess` (System scp Command)

If you already have `scp` installed locally, you can run it directly:

```python
import subprocess

def scp_with_subprocess(local_file, remote_user, remote_host, remote_path):
    try:
        cmd = ["scp", local_file, f"{remote_user}@{remote_host}:{remote_path}"]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            return "File transferred successfully"
        else:
            return f"Error: {result.stderr}"

    except Exception as e:
        return f"Error: {e}"

# Usage
print(scp_with_subprocess("test.txt", "ubuntu", "192.168.1.10", "/home/ubuntu/test.txt"))
```

---

## ✅ When to Use What

* **scp + paramiko** → If you want **native Python automation** with SCP.
* **paramiko SFTP** → If you want SCP-like file transfers but with extra flexibility (list directories, chmod, etc.).
* **subprocess + scp** → Easiest if you already use system `scp` and don’t mind external calls.
