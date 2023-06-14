#!/usr/bin/python3


def roman_to_int(roman_string):
    # intiate dictionary with roman numerals and their values
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}

    if roman_string is None or type(roman_string) is not str:
        return 0
    # if the string is only one character, return the value of that character
    if len(roman_string) == 1:
        for key, value in romans.items():
            if roman_string == key:
                return value
    else:
        total = 0
        for i in range(len(roman_string)):
            for key, value in romans.items():
                if roman_string[i] == key:
                    if i + 1 < len(roman_string):
                        if romans[roman_string[i + 1]] > value:
                            total -= value
                        else:
                            total += value
                    else:
                        total += value
        return total
