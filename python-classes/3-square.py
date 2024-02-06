#!/usr/bin/python3
"""
Create class Square
"""


class Square:
    """
    define Square by size
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """
    define function for return area of square
    """
    def area(self):
        Area_Square = self.__size ** 2
        return Area_Square
