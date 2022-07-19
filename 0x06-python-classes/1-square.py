#!/usr/bin/python3
"""Creates a square

    Attributes:
        Square (class): a class that creates a square
"""


class Square:
    """A Square class with validated private instance attribute size

    Args:
        size (int): size of square
    """

    def __init__(self, size):
        self.__size = size
