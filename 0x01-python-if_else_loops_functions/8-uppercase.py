#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    toUp = ord('a') - ord('A')
    for c in str:
        # if character is not uppercase
        if ord(c) < ord('A') or ord(c) > ord('Z'):
            print("{}".format(chr(ord(c) - toUp)), end="")
        else:
            print("{}".format(c), end="")
    print()
