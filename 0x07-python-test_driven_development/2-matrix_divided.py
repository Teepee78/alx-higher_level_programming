#!/usr/bin/python3
"""This module contains matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides a list of lists of numbers

    Args:
        matrix: list of lists of numbers
        div: number to divide matrix by

    Raises:
        TypeError: if matrix is not list of lists of integers/floats
                    or if div is not an integer or float
        ZeroDivisionError: if div is 0

    Returns:
        a new  list of lists containing the results
    """
    # check if div is a number
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
        return
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check that matrix is a list of lists of numbers
    err = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(err)
        return
    for i, elem in enumerate(matrix):
        if type(elem) is not list or len(elem) == 0:
            raise TypeError(err)
            return
        # get the size of the first list
        if i == 0:
            size = len(elem)
        else:  # compare the size with the first
            if len(elem) != size:
                raise TypeError(err2)
                return
        for i in elem:
            if type(i) not in [int, float]:
                raise TypeError(err)
                return

    result = []

    for row in matrix:
        result.append([round((element / div), 2) for element in row])

    return result
