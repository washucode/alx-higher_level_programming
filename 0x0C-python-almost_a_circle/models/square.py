#!/usr/bin/python3

""" Square class module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns string representation of Square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
