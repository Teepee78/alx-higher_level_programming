#!/usr/bin/python3
"""This module defines a class 'Sqaure'"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square

    Args:
        size: size of rectangle
        x: x coordinate of rectangle
        y: y coordinate of rectangle
        id: id of instance
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string represenation of square"""

        return f"[Square] ({self.id:d}) {self.x:d}/{self.y:d} - {self.width:d}"

    @property
    def size(self):
        """Size of square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is <= 0
        """

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates square attributes"""

        attrs = ["id", "size", "x", "y"]

        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, arg in kwargs.items():
                if key in attrs:
                    setattr(self, key, arg)

    def to_dictionary(self):
        """Returns the dictionary represenation of square"""

        dic = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return dic
