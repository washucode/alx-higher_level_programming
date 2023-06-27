#!/usr/bin/python3

"""Module: 3-square.py - defines a square"""


class Square:
    """defines class Square"""

    def __init__(self, size=0):
        """private attribute size that is optional"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
