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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
            json_string: string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance with attributes set from a dictionary.

        This method creates a "dummy" instance and then updates it
        with the real values from the provided dictionary.

        Args:
            **dictionary: A double pointer to a dictionary containing
                          attributes to set on the instance.

        Returns:
            An instance of cls with attributes set as per dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Load a list of instances from a JSON file.

        This method creates instances based on a JSON file named
        <Class name>.json. If the file doesn't exist, it returns
        an empty list.

        Returns:
            A list of instances of cls.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as file:
                list_dictionaries = cls.from_json_string(file.read())
                return [cls.create(**d) for d in list_dictionaries]
        except FileNotFoundError:
            return []
