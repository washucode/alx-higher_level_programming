#!/usr/bin/python3

"""Read file module"""


def read_file(filename=""):
    """Read a file and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
