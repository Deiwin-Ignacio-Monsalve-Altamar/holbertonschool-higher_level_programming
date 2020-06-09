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
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Create objects from object instances, then save to json file
        Args:
            cls (class): the class of the object instances
            list_objs (list): list of class objects
        """
        with open(cls.__name__ + '.json', mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                objs = [cls.to_dictionary(obj) for obj in list_objs]
                f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns:
            [type]: [description]
        """
        if cls.__name__ == 'Rectangle':
            new_clase = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_clase = cls(1)
        new_clase.update(**dictionary)
        return new_clase

    @classmethod
    def load_from_file(cls):
        """
        Returns:
            [type]: [description]
        """
        filename = cls.__name__ + ".json"
        list_new = []
        with open(filename, mode="r", encoding="UTF-8") as f:
            json_string = f.read()
            new_string = cls.from_json_string(json_string)
            for item in new_string:
                if isinstance(item, dict) is True:
                    list_new.append(cls.create(**item))
                else:
                    list_new.append(item)
        return list_new
