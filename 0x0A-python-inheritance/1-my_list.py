#!/usr/bin/python3
"""This module defines a class 'MyList'"""


class MyList(list):
    """Extends the built in list object"""

    def print_sorted(self):
        """Prints the list, sorted"""
        # copy list
        new_list = self[:]
        # iterate list
        for j in range(len(new_list) - 1, 0, -1):
            for i in range(j):
                # check if value is greater than next value
                if new_list[i] > new_list[i + 1]:
                    # swap the values
                    new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
        print(new_list)
