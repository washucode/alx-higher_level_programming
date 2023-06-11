#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for value in range(len(row)):
                if value == len(row) - 1:
                    print("{:d}".format(row[value]), end="")
                else:
                    print("{:d}".format(row[value]), end=" ")
            print()
