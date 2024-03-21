import smtplib
import ssl
import os


def send_email(message, user_email):
    host = "smtp.gmail.com"
    port = 465

    username = "mosigbadebo@gmail.com"
    password =  os.getenv("PASSWORD")   #"yrnl yawf jmci eqga"

    receiver = user_email   # "tosinoreka@yahoo.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)