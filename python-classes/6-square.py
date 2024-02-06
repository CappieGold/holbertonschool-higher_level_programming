#!/usr/bin/python3
"""
Create class Square
"""


class Square:
    """
    define Square by size
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if (
            not isinstance(value, tuple) or len(value) != 2
            or not all(isinstance(x, int) for x in value)
            or not all(x >= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def area(self):
        Area_Square = self.__size ** 2
        return Area_Square
