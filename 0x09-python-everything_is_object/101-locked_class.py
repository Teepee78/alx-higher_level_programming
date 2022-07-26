#!/usr/bin/python3
"""This module defines a class LockedClass with no class\
 or object attribute, that prevents the user from dynamically creating new \
 instance attributes, except if the new instance attribute is called first_name
"""


class LockedClass:
    """A LockedClass class"""
    def __setattr__(self, attr, value):
        """Set attrbute"""
        if attr != "first_name":
            err = "'LockedClass' object has no attribute '{}'".format(attr)
            raise AttributeError(err)
        self.__dict__.update({attr: value})
