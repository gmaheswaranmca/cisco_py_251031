dir_path = r'C:\Users\gmahe\Downloads' 
attachments = [
    f'{dir_path}/cisco-photo_1.jpeg',
    f'{dir_path}/cisco-photo_2.jpeg',
    f'{dir_path}/cisco-photo_3.jpeg'
]
from mail import send_gmail_attach
from config import to_address 
result = send_gmail_attach(to_address, "Maheswaran - Test Subject from pystud19 - 06-11-2025 - Photos", "Hello from Python!", attachments)
print("Mail sent successfully?" , result)