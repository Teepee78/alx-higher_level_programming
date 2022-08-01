#!/usr/bin/python3
"""This module defines a function 'add_attribute'"""


def add_attribute(obj, attr1, attr2):
    """Tries to add an attribute to a class

    Raises:
        TypeError: if cannot add_attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr1, attr2)
    else:
        raise TypeError("can't add new attribute")
