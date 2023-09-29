#!/usr/bin/python3
"""
    Takes in a URL,displays the body of the response.
    handles HTTPError exceptions to print error codes.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
        Takes in a URL,displays the body of the response.
        handles HTTPError exceptions to print error codes.

        Args:
            url : resource url
    """
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
