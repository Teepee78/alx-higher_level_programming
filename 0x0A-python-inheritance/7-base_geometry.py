#!/usr/bin/python3
"""This module defines a class 'BaseGeometry'"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception with the message
        'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
