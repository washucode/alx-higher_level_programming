#!/usr/bin/python3


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle"""
    triangle = []
    # loop through each row
    for i in range(n):
        row = [1]
        # loop through each column
        for c in range(1,c):
            # append the sum of the two numbers above
            row.append(triangle[i-1][c-1] + triangle[i-1][c])
        if i > 0:
            # append 1 to the end of the row
            row.append(1)
        # append the row to the triangle
        triangle.append(row)
    return triangle