import email, smtplib, ssl, getpass, stdiomask

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#getting sender email
sender_email = input("Please input email: ")
password = stdiomask.getpass("Input your password: ")
mail_content = "Hi this sent from Python"

#read recipient list
f = open("receiver_list.txt", "r+")
receiver_email = [i.strip() for i in f.readlines()]

message = MIMEMultipart()
message ['From'] = sender_email
message ['To'] = ', '.join(receiver_email)
message ['Subject'] = 'Python Email'
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'Final Project - Basic Python.pdf'
attach_file = open('Final Project - Basic Python.pdf', 'rb')
payload = MIMEBase('application', 'octet-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
message.attach(payload)


#log in server
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
print('Mail Sent')