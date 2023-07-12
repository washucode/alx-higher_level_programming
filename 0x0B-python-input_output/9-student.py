#!/usr/bin/python3


"""Student to JSON module"""


class Student:
    """Class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation"""
        if (type(attrs) is list and
                all(type(i) is str for i in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
