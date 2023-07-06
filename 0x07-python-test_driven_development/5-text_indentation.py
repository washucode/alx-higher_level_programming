#!/usr/bin/python3

"""Module that prints a text with 2 new
lines after each of these characters:
., ? and :"""


def text_indentation(text):
    """Function that prints a text with 2 new lines
    after each of these characters:
    ., ? and :
    Args:
        text (str): text to print.
    Returns:
        None
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print(text, end="")
