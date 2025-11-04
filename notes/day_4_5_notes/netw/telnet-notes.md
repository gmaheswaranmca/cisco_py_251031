# to automate **Telnet protocol interactions** using Python.

Telnet is an older text-based network protocol (port 23 by default) that allows you to log in and send commands remotely. Although it’s largely replaced by **SSH** for security, it’s still used in legacy systems, routers, and embedded devices.

---

## 🔑 Key Python Options for Telnet Automation

### 1. **Using `telnetlib` (Standard Library)**

Python’s `telnetlib` module is built-in and great for simple automation.

#### Example: Automating a Telnet Session

```python
import telnetlib

def telnet_automation(host, port, username, password, command):
    try:
        # Open connection
        tn = telnetlib.Telnet(host, port, timeout=10)

        # Login
        tn.read_until(b"login: ")
        tn.write(username.encode("ascii") + b"\n")

        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

        # Run command
        tn.write(command.encode("ascii") + b"\n")
        tn.write(b"exit\n")

        # Get output
        output = tn.read_all().decode("ascii")
        return output

    except Exception as e:
        return f"Error: {e}"

# Usage
result = telnet_automation("192.168.1.1", 23, "admin", "password123", "show running-config")
print(result)
```

---

### 2. **Using `pexpect` (More Control)**

[`pexpect`](https://pexpect.readthedocs.io/) is a Python module for controlling interactive applications. It’s more flexible than `telnetlib`.

```python
import pexpect

def telnet_with_pexpect(host, username, password, command):
    try:
        child = pexpect.spawn(f"telnet {host}")
        child.expect("login: ")
        child.sendline(username)

        child.expect("Password: ")
        child.sendline(password)

        child.expect(r"\$")  # Wait for shell prompt
        child.sendline(command)

        child.expect(r"\$")
        output = child.before.decode("utf-8")

        child.sendline("exit")
        child.close()
        return output

    except Exception as e:
        return f"Error: {e}"

# Usage
print(telnet_with_pexpect("192.168.1.1", "admin", "password123", "ls -l"))
```

---

### 3. **Third-Party Libraries for Network Automation**

* **Netmiko** (built on top of `paramiko`, mainly for network devices, usually SSH but supports Telnet too).
* **Exscript** (scriptable network connections, supports Telnet/SSH).

Example with **Netmiko**:

```python
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "password123",
    "port": 23
}

connection = ConnectHandler(**device)
output = connection.send_command("show ip interface brief")
print(output)
connection.disconnect()
```

---

## ⚠️ Security Note

Telnet sends credentials in **plain text**. If security matters:

* Prefer **SSH automation** (`paramiko`, `netmiko`).
* If stuck with Telnet, use a VPN or secure network.

