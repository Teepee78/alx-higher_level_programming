#!/usr/bin/python3
"""This module defines a Rectangle class based on 7-rectangle.py"""


class Rectangle:
    """A Rectangle class

    Args:
        width: width of rectangle
        height: height of rectangle

    Raises:
        TypeError: if width or height are not integers
        ValueError: if width or height are less than 0
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
            return
        if value < 0:
            raise ValueError("width must be >= 0")
            return
        self.__width = value

    @property
    def height(self):
        """Height of rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
            return
        if value < 0:
            raise ValueError("height must be >= 0")
            return
        self.__height = value

    def area(self):
        """Returns the calculated area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the calculated perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """String represenation of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        row = str(self.print_symbol) * self.width
        for i in range(self.height):
            if i == (self.height - 1):
                rectangle = rectangle + row
            else:
                rectangle = rectangle + row + "\n"
        return rectangle

    def __repr__(self):
        """Represenation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """delete rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle instance"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
            return
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
            return

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
