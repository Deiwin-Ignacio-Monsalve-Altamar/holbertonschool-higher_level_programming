#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import io
import sys

class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        r1 = Rectangle(1, 1)
        self.assertIsInstance(r1, Base)

    def test_rect_id(self):
        r2 = Rectangle(4, 3, 4, 1, 35)
        self.assertEqual(r2.id, 35)
    
    def test_rectangle(self):
        r4 = Rectangle(3, 5, 6, 8, 10)
        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 5)
        self.assertEqual(r4.x, 6)
        self.assertEqual(r4.y, 8)
        self.assertEqual(r4.id, 10)
    
    def test_rectangle_valid_type_error(self):
        self.assertRaises(TypeError, Rectangle, "Deiwin", 1)
        self.assertRaises(TypeError, Rectangle, 1, "Deiwin")
        self.assertRaises(TypeError, Rectangle, [1], 2)
        self.assertRaises(TypeError, Rectangle, 1.1, 1)
        self.assertRaises(TypeError, Rectangle, (1, ) , 1)
        self.assertRaises(TypeError, Rectangle, 1.1, 1, 1, 1)

    def test_rectangle_valid_value_error(self):
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, -100)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 1, -2, 1)

    def test_area(self):
        r4 = Rectangle(2, 2)
        self.assertEqual(r4.area(), 4)

    def test_display(self):
        r5 = Rectangle(3, 3)
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        r5.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n###\n")

    def test_str(self):
        r6 = Rectangle(1, 2)
        list_string = r6.__str__()
        self.assertEqual(list_string, "[Rectangle] (1) 0/0 - 1/2")

    def test_display_1(self):
        r7 = Rectangle(2, 3, 2, 2)
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        r7.display()
        self.assertEqual(sys.stdout.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_update_args(self):
        r11 = Rectangle(9, 9, 9, 9)
        r11.update(89, 2, 3, 4, 5)
        self.assertEqual(r11.width, 2)
        self.assertEqual(r11.height, 3)
        self.assertEqual(r11.x, 4)
        self.assertEqual(r11.y, 5)
        self.assertEqual(r11.id, 89)
        self.assertRaises(TypeError, r11.update, 45, "Deiwin")
        self.assertRaises(TypeError, r11.update, 1, 1, "Monsalve")
        self.assertRaises(TypeError, r11.update, 1, 1, 1, "Altamar")
        self.assertRaises(ValueError, r11.update, 89, -1, 1)
        self.assertRaises(ValueError, r11.update, 89, 1, -1)
        self.assertRaises(ValueError, r11.update, 89, 1, 1, -1)
    
    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(height=1)
        self.assertEqual(r1.height, 1)
    
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)
        self.assertRaises(TypeError, r1.update, x='Holberton')
        self.assertRaises(TypeError, r1.update, y=3.5)
        self.assertRaises(TypeError, r1.update, height=(1,))
        self.assertRaises(TypeError, r1.update, width=[2])
        self.assertRaises(ValueError, r1.update, height=-1)
        self.assertRaises(ValueError, r1.update, width=-1)
        self.assertRaises(ValueError, r1.update, x=-1)
        self.assertRaises(ValueError, r1.update, y=-1)

    def test_to_dict(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        dic_comparation = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, dic_comparation)
        
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1 == r2, False)
