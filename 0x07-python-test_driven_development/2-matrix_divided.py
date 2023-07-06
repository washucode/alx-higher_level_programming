#!/usr/bin/python3

""" Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    Args:
        matrix (list): list of lists of integers or floats.
        div (int/float): number to divide the matrix.
    Returns:
        list: list of lists of integers or floats.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error)
    if len(matrix) == 0:
        raise TypeError(error)
    rows_len = []
    for row in matrix:
        rows_len.append(len(row))
        if type(row) is not list:
            raise TypeError(error)
        if len(row) == 0:
            raise TypeError(error)
        for e in row:
            if type(e) is not int and type(e) is not float:
                raise TypeError(error)
    if len(set(rows_len)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    newMatrix = list(map(lambda row:
                          list(map(lambda e: round(e/div, 2), row)), matrix))
    return newMatrix
