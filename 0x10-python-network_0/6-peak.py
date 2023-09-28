#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    mid_index = len(list_of_integers) // 2
    p_peak = list_of_integers[mid_index]
    if p_peak > list_of_integers[mid_index - 1] and \
       p_peak > list_of_integers[mid_index + 1]:
        return p_peak
    elif p_peak < list_of_integers[mid_index - 1]:
        return find_peak(list_of_integers[:mid_index])
    else:
        return find_peak(list_of_integers[mid_index + 1:])
