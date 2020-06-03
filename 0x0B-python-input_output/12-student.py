#!/usr/bin/python3


"class function students"


class Student:
    """class studnets
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

        mylist = {}

        for att in attrs:
            if att in self.__dict__:
                mylist[att] = self.__dict__[att]
        return mylist
