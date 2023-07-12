#!/usr/bin/python3

"""
Module for my_list class
"""


class MyList(list):
    """ MyList class inherits from list """

    def print_sorted(self):
        """ Print the list, but sorted (ascending sort) """
        print(sorted(self))



