#!/usr/bin/python3
""" Convert JSON string to Python object. """


def from_json_string(my_str):
    """ Convert a JSON string to a Python object.

    Args:
        my_str (str): JSON string to be converted.

    Returns:
        object: Corresponding Python object.
    """
    import json
    return json.loads(my_str)
