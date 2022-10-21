#!/usr/bin/python3
"""
This module Takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""
import requests
from sys import argv


if __name__ == '__main__':
    response = requests.get(argv[1])
    code = response.status_code
    if code > 400:
        print(f"Error code: {code}")
    else:
        print(response.text)
