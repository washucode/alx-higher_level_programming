#!/usr/bin/python3
"""Task 1: Defines a class Rectangle.
"""


class Rectangle:
    """class creates private instance attributes width and height
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """init method initializes y private instance attributes"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """__height getter method retrieves the height
        Args:
            self: instance method
        Return:
            __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height is int and is positive
        Args:
            value (int): height of the rectangle
        Raises:
                TypeError: height must be an integer
                ValueError: height must be >= 0
        returns:
            height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    @property
    def width(self):
        """__width getter method retrieves the width
        Args:
            self: instance method
        Return:
            __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width is int and is positive
        Args:
            value (int): width of the rectangle
            Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
        returns:
            width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value
