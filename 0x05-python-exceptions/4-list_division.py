#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists."""
    newlist = []
    result = 0

    for e in range(list_length):
        try:
            result = my_list_1[e] / my_list_2[e]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            newlist.append(result)
    return newlist
