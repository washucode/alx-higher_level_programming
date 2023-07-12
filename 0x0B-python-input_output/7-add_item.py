#!/usr/bin/python3

"""Add item module"""
import sys
from os import path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    if path.exists(filename):
        pylist = load_from_json_file(filename)
    else:
        pylistlist = []
    for i in range(1, len(sys.argv)):
        pylist.append(sys.argv[i])
    save_to_json_file(pylist, filename)
