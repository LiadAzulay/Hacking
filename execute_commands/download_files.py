#!/usr/bin/env python
import requests


def download(url):
    # Getting response using requsts 'GET'
    get_response = requests.get(url)
    # Getting file name
    file_name = url.split("/")[-1]
    # Saving answer to file
    with open("sample.txt", "w") as out_file:
        out_file.write(get_response.content)
