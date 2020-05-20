#!/usr/bin/python3
"Defining math"
import math


class MagicClass:
    "Defining math"
    def __init__(self, radius):
        "Defining math"
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        "Defining math"
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        "Defining math"
        return 2 * math.pi * self._MagicClass__radius
