#!/usr/bin/python3
"""Creates a square"""


class Square:
    """A Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square

        Args:
            size: size of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Size of square"""
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

    @property
    def position(self):
        """position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter

        Args:
            poition of square
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple with 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple with 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple with 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Area of Square

        Returns:
            size ** 2
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
