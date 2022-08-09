#!/usr/bin/python3
"""This module defines a class 'Rectangle'"""
from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle

    Args:
        width: width of rectangle
        height: height of rectangle
        x: x coordinate of rectangle
        y: y coordinate of rectangle
        id: id of instance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns the string represenation of the rectangle"""

        return f"[Rectangle] ({self.id:d}) {self.x:d}/{self.y:d} - \
{self.width:d}/{self.height:d}"

    @property
    def width(self):
        """Width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width <= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Height of rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height <= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x coordinate of rectangle

        Raises:
            TypeError: if x is not an integer
            ValueError: if x < 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y coordinate of rectangle

        Raises:
            TypeError: if y is not an integer
            ValueError: if y < 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, attr, value):
        """Validates value to be an integer

        Raises:
            TypeError: if value is not an integer
            ValueError: if width or height <= 0 or if x or y < 0
        """

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(attr))
        if (attr == "width" or attr == "height") and value <= 0:
            raise ValueError("{:s} must be > 0".format(attr))
        if (attr == "x" or attr == "y") and value < 0:
            raise ValueError("{:s} must be >= 0".format(attr))

    def area(self):
        """Returns the calculated area of rectangle"""

        return self.width * self.height

    def display(self):
        """Prints the rectangle with a symbol"""

        string = "{}{:s}".format(" " * self.x, "#" * self.width)
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(string)

    def update(self, *args, **kwargs):
        """Updates the rectangle attributes"""

        attrs = ['id', 'width', 'height', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, arg in kwargs.items():
                if key in attrs:
                    setattr(self, key, arg)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""

        dic = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dic
