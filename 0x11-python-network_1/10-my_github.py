#!/usr/bin/python3
"""
This module takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]

    response = requests.get(
        "https://api.github.com/user",
        params={'login': username},
        auth=(username, password)
    )

    if "id" in response.json():
        print(response.json()['id'])
    else:
        print(None)
