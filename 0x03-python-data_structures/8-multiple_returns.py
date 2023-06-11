#!/usr/bin/python3


def multiple_returns(sentence):
    # Returns a tuple with the length of a string and its first character.
    # if sentence is empty
    if len(sentence) == 0:
        return (0, None)

    # if sentence is not empty
    return (len(sentence), sentence[0])
