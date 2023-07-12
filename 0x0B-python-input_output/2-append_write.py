#!/usr/bin/python3

"""Append to a file module"""


def append_write(filename="", text=""):
    """Append a file and print the number of characters appended"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
