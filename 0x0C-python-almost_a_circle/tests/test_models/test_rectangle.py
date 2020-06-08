#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import io

class TestRectangle(unittest.TestCase):

    def setUp(self):
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
        r3 = Rectangle(2, 2)
        self.assertEqual(r3.area(), 4)

    def test_display(self):
        sys.stdout = io.StringIO()
        r1 = Rectangle(3, 3)
        r1.display()
        assertEqual(sys.stdout.getvalue(), "###\n###\n###\n")


