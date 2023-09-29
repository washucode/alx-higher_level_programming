#!/usr/bin/python3
"""
    Takes in a URL, sends a request to the URL and displays the body of the
    response.
    if the HTTP status code is greater than or equal to 400, print: Error code:
    followed by the value of the HTTP status code
"""

import requests
import sys


def fetch_url(url):
    """
        Takes in a URL, sends a request to the URL and displays the body of the
        response.
        if the HTTP status code is greater than or equal to 400, print: Error
        code: followed by the value of the HTTP status code

        Args:
            url : resource url
    """
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
