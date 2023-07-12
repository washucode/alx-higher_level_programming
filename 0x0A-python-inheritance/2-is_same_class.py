#!/usr/bin/python3

""" is_same_class module """


def is_same_class(obj, a_class):
    """ Return True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    return type(obj) == a_class
