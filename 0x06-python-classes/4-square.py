#!/usr/bin/python3
"""Creates a square"""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """Size property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size property setter

        Args:
            value: value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """Area of Square

        Returns:
            size ** 2
        """
        return self.__size ** 2
