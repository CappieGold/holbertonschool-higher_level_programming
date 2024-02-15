#!/usr/bin/python3
""" Module for converting objects to JSON strings. """


def to_json_string(my_obj):
    """ Converts a Python object to a JSON string.

    Args:
        my_obj: A Python object (like a list or a dictionary).

    Returns:
        str: The JSON string representation of my_obj.
    """
    import json
    return json.dumps(my_obj)
