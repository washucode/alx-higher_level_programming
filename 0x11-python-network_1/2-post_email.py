#!/usr/bin/python3
"""
    Takes in a URL, sends a POST REQUEST to the passed URL with the email as a
    parameter, and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


def post_request(url, email):

    try:
        values = {'email': email}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode("utf-8"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_request(url, email)
