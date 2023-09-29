#!/usr/bin/python3
"""
    Takes in a URL,displays the body of the response.
    displayes the value of the X-Request-Id variable found in the header of the
    response.
"""

import requests
import sys


def fetch_url(url):
    """
        Takes in a URL,displays the body of the response.
        displayes the value of the X-Request-Id variable found in the header of
        the response.

        Args:
            url : resource url
    """
    r = requests.get(url)
    print(r.headers['X-Request-Id'])


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
