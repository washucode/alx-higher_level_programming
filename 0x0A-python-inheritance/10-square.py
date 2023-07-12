#!/usr/bin/python3

""" Square Module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize Square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
