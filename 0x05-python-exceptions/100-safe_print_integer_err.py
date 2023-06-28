#!/usr/bin/python3


def safe_print_integer_err(value):
    """a function that prints an integer with "{:d}".format()"""
    try:
        print("{:d}".format(value))
        return True

    except (ValueError, TypeError) as thiserror:
        import sys
        print("Exception: {}".format(thiserror), file=sys.stderr)
        return False
