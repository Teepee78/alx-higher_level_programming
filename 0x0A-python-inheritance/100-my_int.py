#!/usr/bin/python3
"""This module defines a class 'MyInt'"""


class MyInt(int):
    """This class inverts == and != operators"""

    def __eq__(self, other):
        """inverts =="""
        return not super().__eq__(other)

    def __ne__(self, other):
        """inverts !="""
        return not super().__ne__(other)
