#!/usr/bin/python3

""" MyInt Module """


class MyInt(int):
    """ MyInt class """

    def __eq__(self, other):
        """ Return True if self and other are not equal """
        return int(self) != int(other)

    def __ne__(self, other):
        """ Return True if self and other are equal """
        return int(self) == int(other)
