#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return 0

    rom_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    length = len(roman_string)
    number = 0
    i = 0
    while i < length:
        if i < (length - 1) and rom_num[roman_string[i]] < rom_num[roman_string[i + 1]]:
            number += rom_num[roman_string[i + 1]] - rom_num[roman_string[i]]
            i += 1
        else:
            number += rom_num[roman_string[i]]
        i += 1
    return number
