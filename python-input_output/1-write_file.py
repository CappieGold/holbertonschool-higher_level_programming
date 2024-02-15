#!/usr/bin/python3
""" Module for writing text to a file. """


def write_file(filename="", text=""):
    """ Writes a string to a text file and returns its length.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: The length of the text written.
    """
    with open(filename, 'w') as file:
        file.write(text)
    return len(text)
