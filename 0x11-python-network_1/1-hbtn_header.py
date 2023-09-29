#!/usr/bin/python3
"""
    Takes  a URL, sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def header_request(url):
    """
        Takes  a URL, sends a request to the URL and displays the value of the
        X-Request-Id variable found in the header of the response.

        Args:
            url : resource url
    """
    try:
        with urllib.request.urlopen(url) as response:
            header = response.info()
            print(header['X-Request-Id'])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = sys.argv[1]
    header_request(url)
