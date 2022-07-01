#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints a list of integers in reverse order

    Args:
        my_list: list of integers
    """
    lenList = len(my_list)

    if lenList == 0:
        return

    idx = lenList - 1
    while idx > 0:
        print("{:d}".format(my_list[idx]))
        i -= 1
