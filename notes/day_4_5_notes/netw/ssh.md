## 🔑 Python Options for SSH Automation

### 1. **Paramiko (Most Common)**

[Paramiko](http://www.paramiko.org/) is a Python library for SSH connections.

#### Example: Run Commands via SSH

```python
import paramiko

def ssh_command(host, port, username, password, command):
    try:
        # Create SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect
        client.connect(host, port=port, username=username, password=password)

        # Run command
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        client.close()
        return output if output else error

    except Exception as e:
        return f"Error: {e}"

# Usage
print(ssh_command("192.168.1.10", 22, "ubuntu", "password123", "ls -l"))
```

---

### 2. **Using SSH Keys Instead of Passwords**

More secure than passwords:

```python
import paramiko

def ssh_with_key(host, username, key_file, command):
    try:
        key = paramiko.RSAKey.from_private_key_file(key_file)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(host, username=username, pkey=key)

        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()

        client.close()
        return output

    except Exception as e:
        return f"Error: {e}"

# Usage
print(ssh_with_key("192.168.1.10", "ubuntu", "/home/user/.ssh/id_rsa", "uname -a"))
```

---

### 3. **Netmiko (for Network Devices)**

[Netmiko](https://github.com/ktbyers/netmiko) is built on Paramiko and optimized for routers/switches.

```python
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "password123",
    "port": 22
}

connection = ConnectHandler(**device)
output = connection.send_command("show running-config")
print(output)
connection.disconnect()
```

---

### 4. **Fabric (for Deployment/Multiple Servers)**

[Fabric](https://www.fabfile.org/) builds on Paramiko and is used for running commands on **multiple servers at once**.

```python
from fabric import Connection

c = Connection(host="192.168.1.10", user="ubuntu", connect_kwargs={"password": "password123"})
result = c.run("df -h", hide=True)
print(result.stdout.strip())
```

---

## ✅ Summary

* **Paramiko** → Best for general SSH automation (single host).
* **Netmiko** → Best for routers/switches (Cisco, Juniper, etc.).
* **Fabric** → Best for running commands across multiple servers.
