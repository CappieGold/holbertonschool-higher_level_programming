#!/usr/bin/python3
"""Simple Python script to load data from a JSON file into a Python object."""

import json


def load_from_json_file(filename):
    """Load data from a JSON file and return as a Python object.

    Args:
        filename (str): The path to the JSON file to be read.

    Returns:
        object: The Python object obtained from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
