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

    def test_area(self):
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_square_display(self):
        s1 = Square(2)
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        string_test = s1.__str__()
        s1.display()
        self.assertEqual(string_test, "[Square] (1) 0/0 - 2")
        self.assertEqual(s1.area(), 4)
        self.assertEqual(sys.stdout.getvalue(), "##\n##\n")

    def test_display_espacies(self):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        s2 = Square(2, 2, 2)
        s2.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n")

    def test_update_args(self):
        s11 = Square(9, 9, 9)
        s11.update(89, 2, 3, 4)
        self.assertEqual(s11.size, 2)
        self.assertEqual(s11.x, 3)
        self.assertEqual(s11.y, 4)
        self.assertEqual(s11.id, 89)
        self.assertRaises(TypeError, s11.update, 45, "Deiwin")
        self.assertRaises(TypeError, s11.update, 1, 1, "Monsalve")
        self.assertRaises(TypeError, s11.update, 1, 1, 1, "Altamar")
        self.assertRaises(ValueError, s11.update, 89, -1, 1)
        self.assertRaises(ValueError, s11.update, 89, 1, -1)
        self.assertRaises(ValueError, s11.update, 89, 1, 1, -1)

    def test_update_kwargs(self):
        r1 = Square(10, 10, 10)

        r1.update(size=1)
        self.assertEqual(r1.size, 1)

        r1.update(size=1, x=2)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)
        self.assertRaises(TypeError, r1.update, x='Holberton')
        self.assertRaises(TypeError, r1.update, y=3.5)
        self.assertRaises(TypeError, r1.update, size=(1,))
        self.assertRaises(ValueError, r1.update, size=-1)
        self.assertRaises(ValueError, r1.update, x=-1)
        self.assertRaises(ValueError, r1.update, y=-1)

    def test_to_dict(self):
        s1 = Square(10, 1, 9)
        s1_dictionary = s1.to_dictionary()
        dic_comparation = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
        self.assertEqual(s1_dictionary, dic_comparation)

        s2 = Rectangle(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1 == s2, False)


if __name__ == '__main__':
    unittest.main()
