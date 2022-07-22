#!/usr/bin/python3
"""This module contains print_square function"""


def print_square(size):
    """This function prints a square with the char #

    Args:
        size: a +ve number that is the size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
        return
    if size < 0:
        raise ValueError("size must be >= 0")
        return

    for i in range(size):
        print("{}".format("#" * size))
