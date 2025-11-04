import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import app_password, from_address, to_address

def send_gmail(to_address, subject, body):
    # Your Gmail address and App Password
    
    #from_address = "your_email@gmail.com"
    #app_password = "your_app_password"  # generate in Google Account -> Security -> App passwords
    

    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, app_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Error:", e)
        return False

#to_address = "receiver_username@gmail.com"
result = send_gmail(to_address, "Test Subject", "Hello from Python!")
print("Mail sent successfully?" , result)
