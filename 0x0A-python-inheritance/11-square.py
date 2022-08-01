#!/usr/bin/python3
"""This module defines a class 'Square'"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle

    Args:
        size: size of square
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
