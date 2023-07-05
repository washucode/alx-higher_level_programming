#!/usr/bin/python3
class LockedClass:
    """LockedClass prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """__init__ initializes the LockedClass instance.
        Args:
            first_name (str): the first name of the LockedClass instance.
        """
        self.first_name = first_name

    def __setattr__(self, name, value):
        """__setattr__ sets the LockedClass instance's attributes.
        """
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 name + "'")
        self.__dict__[name] = value
