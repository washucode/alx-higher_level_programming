#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    # a function that returns a new dictionary values * 2
    return {key: value * 2 for key, value in a_dictionary.items()}
