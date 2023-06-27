#!/usr/bin/python3
"""Module: 6-square.py - defines a square"""


class Square:
    """defines class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """private attribute size that is optional"""
        self.__size = size
        self.__position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.size):
                for y in range(self.position[0]):
                    print(" ", end="")
                for y in range(self.size):
                    print("#", end="")
                print()
