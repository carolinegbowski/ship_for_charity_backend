import smtplib
import ssl
from password import password


port = 465
smtp_server = "smtp.gmail.com"
sender_email = "ship4charity@gmail.com"
receiver_email = email
password = password()
context = ssl.create_default_context()
message = """\
Subject: Test

This worked!"""

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
