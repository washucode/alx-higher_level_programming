#!/usr/bin/python3

"""Append after module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a string"""
    with open(filename, "r+") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
        f.seek(0)
        f.writelines(lines)
