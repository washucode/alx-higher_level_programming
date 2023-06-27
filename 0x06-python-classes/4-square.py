#!/usr/bin/python3
"""Module: 4-square.py - defines a square"""


class Square:
    """defines class Square"""

    def __init__(self, size=0):
        """private attribute size that is optional"""
        self.__size = size

    def area(self):
        """returns the square area"""
        return self.__size ** 2

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value
