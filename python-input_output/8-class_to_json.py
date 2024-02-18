#!/usr/bin/python3
"""This module defines the function (class_to_json)"""


def class_to_json(obj):
    """Return the dictionnary description of the instance 'obj'

    Args:
        obj(class): Is an instance of a Class.
    """
    return obj.__dict__
