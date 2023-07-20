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

    def update(self, *args, **kwargs):
        """ Updates attributes of Square """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def size(self):
        """ Getter for size """
        return self.width
 
    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value
