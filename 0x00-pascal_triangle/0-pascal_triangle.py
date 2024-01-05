#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for x in range(n):
        temp_list = []

        for y in range(i+1):
            if y == 0 or y == x:
                temp_list.append(1)
            else:
                temp_list.append(triangle[x-1][y-1] + triangle[x-1][y])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
