#!/usr/bin/python3
"""
This module takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.request as request
import urllib.parse as parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode(encoding='utf-8'))
