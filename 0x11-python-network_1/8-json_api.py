#!/usr/bin/python3
"""
    Takes in a URL, sends a POST request to the URL and
    displays the body of the response.
    letter q is sent as a parameter.
    Using the packages requests and sys
"""

import requests
import sys


def post_request(url, q):
    """
        Takes in a URL, sends a POST request to the URL and displays
        the body of the response.letter q is sent as a parameter.

        Args:
            url : resource url
            q : letter to post
    """
    try:
        payload = {'q': q}
        r = requests.post(url, data=payload)
        if r.json():
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
        else:
            print("No result")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    post_request(url, q)
