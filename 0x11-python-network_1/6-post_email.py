#!/usr/bin/python3
"""
    Takes in a URL and an email, sends a POST request
    to the passed URL with the
    email as a parameter, and displays the body of the response.
    Using the packages requests and sys
"""

import requests
import sys


def post_request(url, email):
    """
        Takes in a URL and an email, sends a POST request to the passed URL
        with the email as a parameter, and displays the body of the response.

        Args:
            url : resource url
            email : email to post
    """
    try:
        payload = {'email': email}
        r = requests.post(url, data=payload)
        print(r.text)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_request(url, email)
