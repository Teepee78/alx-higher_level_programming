#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error:
        from sys import stderr as err
        err.write("Exception: {}\n".format(err))
        return None
