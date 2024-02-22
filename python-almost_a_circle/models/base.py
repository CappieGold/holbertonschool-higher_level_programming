#!/usr/bin/python3
"""Module for class Base"""

import json


class Base:
    """ Base class for future models. Manages id assignment. """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of Base.

        Args:
            id (int, optional): The id of the object. If not provided, it's
            automatically assigned based on __nb_objects.

        Attributes:
            id (int): The public id of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of Base instances to a JSON file.

        Args:
            list_objs (list): A list of inherited instances from Base.
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_string)
