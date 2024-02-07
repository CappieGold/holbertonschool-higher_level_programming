#!/usr/bin/python3
"""
say my name
author: Carpentier
date: 07/02/2024
"""


def say_my_name(first_name, last_name=""):
    """
    print my name with error message if not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
