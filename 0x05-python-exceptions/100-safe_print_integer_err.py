#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        from sys import stderr as err
        err.write("Exception: {}\n".format(error))
        return False
