#!/usr/bin/python3


"class Students"


class Students:
    """class students
    """

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name ([type]): [description]
            last_name ([type]): [description]
            age ([type]): [description]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Args:
            attrs ([type], optional): [description]. Defaults to None.
        """
        if attrs is None:
            return self.__dict__
        
        myDict = {}
        for attr in attrs:
            if attr in self.__dict__:
                myDict[attr] == __dict__[attr]
        return myDict

    def reload_from_json(self, json):
        """
        Args:
            json ([type]): [description]
        """
        if not json:
            return
        self.__dict__ = json
