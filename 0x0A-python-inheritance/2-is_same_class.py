#!/usr/bin/python3
"""This module defines a function 'is_same_class'"""


def is_same_class(obj, a_class):
    """
    Returns True if the object specified is exactly an instance
    of the specified class
    """
    return type(obj) == a_class
