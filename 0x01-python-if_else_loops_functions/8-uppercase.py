#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 122:
            ret = ord(str[char]) - 32
        else:
            ret = ord(str[char])
        print("{:c}".format(ret), end="")
    print("")
