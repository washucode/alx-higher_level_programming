#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 122:
            print("{}".format(chr(ord(str[char]) - 32)), end="")
        else:
            print("{}".format(str[char]), end="")
    print("")
