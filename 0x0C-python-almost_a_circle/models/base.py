#!/usr/bin/python3
""" Class Base"""
import json


class Base:
    """class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """
        Args:
            list_objs ([type]): [description]
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                objs = [cls.to_dictionary(obj) for obj in list_dictionaries]
                f.write(cls-to_json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string is None or json_string is []:
            return "[]"
        return json.loads(json_string)
