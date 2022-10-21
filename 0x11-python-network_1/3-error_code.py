#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request as request
import urllib.parse as parse
import urllib.error as error


if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode(encoding='utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
