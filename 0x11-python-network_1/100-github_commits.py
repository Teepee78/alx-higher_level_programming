#!/usr/bin/python3
"""
This module lists the last 10 commits from a github repo
"""
from sys import argv
import requests


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]

    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/commits",
    )
    if response.status_code < 400:
        commits = response.json()
        i = 0
        try:
            while i < 10:
                co = commits[i]
                name = co.get('commit').get('author').get('name')
                print(f"{co.get('sha')}: {name}")
                i += 1
        except IndexError:
            pass
