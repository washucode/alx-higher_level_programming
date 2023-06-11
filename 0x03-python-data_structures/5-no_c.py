#!/usr/bin/python3


def no_c(my_string):
    n_string = ""
    for index in range(len(my_string)):
        if my_string[index] != 'c' and my_string[index] != 'C':
            n_string += my_string[index]
    return n_string
