#!/usr/bin/python3

""" Module that contains the function add_attribute """

def add_attribute(obj, name, value):
    """ Add a new attribute to an object if its possible """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
