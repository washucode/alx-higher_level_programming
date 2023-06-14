#!/usr/bin/python3


def roman_to_int(roman_string):
    # check if roman_string is None or not a string
    if roman_string is None or type(roman_string) is not str:
        return 0
    # initiate dictionary with roman numerals
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev = 0
    # iterate through roman_stringvixx
    for i in reversed(roman_string):
        comp_val = romans.get(i, 0)
        # if value of current roman numeral is less than previous
        if comp_val < prev:
            num -= comp_val
        # else add value of current roman numeral to num vixx
        else:
            num += comp_val
        prev = comp_val
    return num 