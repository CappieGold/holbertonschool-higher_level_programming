#!/usr/bin/python3
""" Module for reading file contents. """


def read_file(filename=""):
    """ Reads and prints the contents of a file.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content, end='')
