#!/usr/bin/python3


"""class a Student"""


class Student:
    """Create s student class
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

    def to_json(self):
        """
        Returns:
            [type]: [description]
        """
        return self.__dict__
