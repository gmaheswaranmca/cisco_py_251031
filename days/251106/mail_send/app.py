from mail import send_gmail
from config import to_address 
result = send_gmail(to_address, "Maheswaran - Test Subject from pystud19 - 06-11-2025", "Hello from Python!")
print("Mail sent successfully?" , result)