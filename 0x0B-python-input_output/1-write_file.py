#!/usr/bin/python3

"""Write file module"""


def write_file(filename="", text=""):
    """Write a file and print the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
