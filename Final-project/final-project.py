import email, smtplib, ssl, getpass, stdiomask

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#content


#getting sender email
email = input("Masukkan email: ")
password = stdiomask.getpass("Masukkan password: ")
message = "Hi this sent from Python"

#read recipient list
f = open("receiver_list.txt", "r+")
receiver_email = [i.strip() for i in f.readlines()]


#log in server
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email, password)
    server.sendmail(email, receiver_email, message)