#!/usr/bin/python3
"""Module for class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate.
            y (int): The y coordinate.
            id (int): The id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square and update width and height."""
        self.width = value
        self.height = value
        super().width

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update attributes of the square.

        Args:
            *args (tuple): New attribute values,
            in order of 'id', 'size', 'x', 'y'.
            **kwargs (dict): New attribute values as key-value pairs.
        """
        attributes = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for attr, arg in zip(attributes, args):
                setattr(self, attr, arg)
        else:
            for attrk, value in kwargs.items():
                setattr(self, attrk, value)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
