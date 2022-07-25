#!/usr/bin/python3
"""This module contains a function text_indentation"""


def text_indentation(text):
    """This function prints a text with 2 new lines at the end of each of the
    characters . , ? and :

    Args:
        text: string to be printed

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
        return

    newline = True
    for char in text:
        if char in [".", "?", ":"]:
            print("{}\n".format(char))
            newline = True
            continue
        if newline and char != ' ':
            print("{}".format(char), end="")
            newline = False
            continue
        if not newline:
            print("{}".format(char), end="")
            continue
