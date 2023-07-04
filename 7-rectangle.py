#!usr/bin/python3
"""Defines a class Rectangle."""

class Rectangle:
    """ Class creates private instance attributes width and height
    Attributes:
        width: width of the rectangle
        height: height of the rectangle
    Functions:
        __init__(self, width=0, height=0): initializes width and height
        width(self): getter method retrieves the width
        width(self, value): setter method sets the width
        height(self): getter method retrieves the height
        height(self, value): setter method sets the height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes width and height"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """__height getter method retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height is int and is positive
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    @property
    def width(self):
        """__width getter method retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width is int and is positive"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
    
    def __str__(self):
        """prints the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return ((str(self.print_symbol) * self.__width) + "\n") * self.__height
    
    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        """prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
