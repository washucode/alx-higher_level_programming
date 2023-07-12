#!/usr/bin/python3

"""Add item module"""
import json
import sys
from os import path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item(args):
    """Add all arguments to a Python list, and then save them to a file"""
    filename = "add_item.json"
    if path.exists(filename):
        pylist = load_from_json_file(filename)
    else:
        pylist = []
    pylist.extend(sys.argv[1:])
    save_to_json_file(pylist, filename)
