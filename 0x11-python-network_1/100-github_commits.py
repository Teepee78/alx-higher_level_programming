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
    commits = response.json()
    i = 0
    while i < 10:
        co = commits[i]
        print(
            f"{co.get('sha')}: {co[i].\
            get('commit').get('author').get('name')}"
        )
        i += 1
