#!/usr/bin/python3


def main():
    from sys import argv

    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc))
        for x in range(1, argc + 1):
            print("{}: {}".format(x, argv[x]))


if __name__ == "__main__":
    main()
