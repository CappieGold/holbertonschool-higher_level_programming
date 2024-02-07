#!/usr/bin/python3
"""
print square
author: Carpentier
Date: 07/02/2024
"""


def print_square(size):
    """
    print square with error if float and < 0
    """
    if  not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
