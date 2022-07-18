#!/usr/bin/python3
from sys import stderr as err


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error:
        err.write("Exception: {}\n".format(error))
        return None
