#!/usr/bin/env python

import requests


def request(url):
    try:

        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"

# Using brute force to found subdomains
with open("/root/subdomains.txt", "r") as file:
    for line in file:
        # Removing \n
        word = line.strip()
        # Appending subdomain name and target
        test_url = word + "." + target_url
        # Checking response
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)
