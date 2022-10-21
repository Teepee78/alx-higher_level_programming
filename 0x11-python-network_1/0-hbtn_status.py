#!/usr/bin/python3
"""This module fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as urllib


if __name__ == '__main__':
    with urllib.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode(encoding='utf-8')}")
