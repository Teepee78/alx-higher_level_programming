#!/usr/bin/python3
"""Creates a square

Attributes:
        Square (class): a class that creates a square
"""


class Square:
    """A Square class with validated private instance attribute size

    Args:
        size (int): size of square
        position (tuple): position of Square on a grid
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position: position of square

        setter validates position is a tuple of positive integers

        Raises:
            TypeError: if position is not a tuple of 2 +ve ints
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not self.__checkPosition(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __checkPosition(self, position):
        """Checks if position is a tuple of two positive integers

        Returns: True if position is valid, False otherwise
        """
        if type(position) is not tuple or len(position) != 2:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        else:
            return True

    def area(self):
        """Area of Square

        Returns:
            size ** 2
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with #"""
        x = self.__position[0]
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("{}{}".format(" " * x, "#" * self.__size))

    def __str__(self):
        """Returns string version of square"""
        if self.__size == 0:
            return ""
        string = "\n" * self.position[1]
        for i in range(self.__size):
            string = string + "{}{}".format(" ", "#" * self.__size)
            if i < self.__size - 1:
                string = string + "\n"
        return string
