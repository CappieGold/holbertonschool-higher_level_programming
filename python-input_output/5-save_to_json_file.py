#!/usr/bin/python3
""" Save object to a file as JSON string. """

import json


def save_to_json_file(my_obj, filename):
    """ Save a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The file to write the JSON string to.
    """
    content_write = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(content_write)
