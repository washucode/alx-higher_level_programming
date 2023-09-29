#!/usr/bin/python3
"""
    Takes your Github credentials (username and password)
    and uses the Github.
"""

import requests
import sys


def fetch_url(url, username, password):
    """
        Takes your Github credentials (username and password)
        and uses the Github API to display your id
        Args:
            url : resource url
            username : github username
            password : github password
    """
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json()['id'])
    except Exception as e:
        print('None')


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    fetch_url(url, username, password)
