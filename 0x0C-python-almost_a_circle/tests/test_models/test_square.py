#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import io
import sys

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_inherencia(self):
        s1 = Square(1)
        self.assertIsInstance(s1, Rectangle)

    def test_square_id(self):
        s2 = Square(3)
        self.assertEqual(s2.id, 1)

if __name__ == "__main__":
    
    def test_square_width_and_heigth(self):
        s2 = Square(3)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 3)

    def test_square_x_and_y(self):
        s3 = Square(5, 1, 1)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 1)

    def validation_type_or_value(self):
        self.assertRaises(TypeError, Square, 1, "Holberton")
        self.assertRaises(TypeError, Square, (1, ), 1)
        self.assertRaises(TypeError, Square, [1], 1)        
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaises(ValueError, Square, -1, 1)
        self.assertRaises(ValueError, Square, 3.5, 5)

    def test_square(self):
        s1 = Square(2)
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        string_test = s1.__str__()
        self.assertEqual(string_test, "[Square] (1) 0/0 - 2")
        self.assertEqual(s1.area(), 4)
"""         self.assertEqual(sys.stdout.getvalue(), "##\n##") """


"""     print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display() """