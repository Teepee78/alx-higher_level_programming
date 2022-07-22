#!/usr/bin/python3
"""This module contains a function to add 2 integers"""


def add_integer(a, b=98):
    """Adds 2 numbers and returns the result

    Args:
        a: first number
        b: second number

    Raises:
        TypeError: if a or b is not a number
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
        return
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
        return

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
