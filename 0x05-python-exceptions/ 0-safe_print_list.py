#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list"""
    try:
        for e in range(x):
            print("{}".format(my_list[e]), end="")
        print()
        return x
    except IndexError:
        print()
        return e
