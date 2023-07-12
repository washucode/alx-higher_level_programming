#!/usr/bin/python3

""" Rectangle Module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
