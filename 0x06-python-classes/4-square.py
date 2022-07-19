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
        """Size of square

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
        """Area of Square

        Returns:
            the area of square
        """
        return self.__size ** 2
