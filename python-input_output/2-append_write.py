#!/usr/bin/python3
""" Module to append text to a file. """


def append_write(filename="", text=""):
    """ Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    """
    with open(filename, 'a') as file:
        file.write(text)
    return len(text)
