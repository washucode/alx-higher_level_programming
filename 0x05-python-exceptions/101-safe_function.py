#!/usr/bin/python3


def safe_function(fct, *args):
    """a function that executes a function safely."""
    try:
        return fct(*args)
    except Exception as excpt:
        print("Exception: {}".format(excpt), file=sys.stderr)
        return None
