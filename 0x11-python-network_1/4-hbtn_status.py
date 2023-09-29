#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status
    using Requests package
"""

import requests


def fetch_url(url):
    html = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
    html.close()


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    fetch_url(url)
