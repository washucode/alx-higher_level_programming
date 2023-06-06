#!/usr/bin/python3
for alpha in range(122, 96, -1):
    if alpha % 2 == 0:
        res = alpha
    else:
        res = alpha - 32
    print("{:c}".format(res), end="")
