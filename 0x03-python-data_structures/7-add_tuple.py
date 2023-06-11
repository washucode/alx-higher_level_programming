#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # if tuple_a < 2
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    # if tuple_b < 2
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    # add the first integers
    first_sum = tuple_a[0] + tuple_b[0]
    # add the second integers
    second_sum = tuple_a[1] + tuple_b[1]
    # return the tuple
    return (first_sum, second_sum)
