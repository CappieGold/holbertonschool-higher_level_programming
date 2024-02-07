#!/usr/bin/python3
"""
This module provides an add_integer function for adding two numbers.
if a and b are int and float
print error message
"""
def add_integer(a, b=98):
    """
    isinstance a,b are int and float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
