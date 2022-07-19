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

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """size: size of square

        setter validates size is an integer and >= 0

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the calculated area of square instance"""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two Squares are equal

        Args:
            other: Square to compare to current instance
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """Checks if two Squares are not equal

        Args:
            other: Square to compare to current instance
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """Checks if current Square is greater than other Square

        Args:
            other: Square to compare to current instance
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """Checks if current Square is greater than or equal to other Square

        Args:
            other: Square to compare to current instance
        """
        return self.__size >= other.__size

    def __lt__(self, other):
        """Checks if current Square is less than other Square

        Args:
            other: Square to compare to current instance
        """
        return self.__size < other.__size

    def __le__(self, other):
        """Checks if current Square is less than or equal to other Square

        Args:
            other: Square to compare to current instance
        """
        return self.__size <= other.__size
