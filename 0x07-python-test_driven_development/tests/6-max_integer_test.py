#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        my_list = [1, 2, 3, 4]
        result = max_integer(my_list)
        self.assertEqual(result, 4)

    def test_negative(self):
        my_list = [-1, -33, -78, -80]
        result = max_integer(my_list)
        self.assertEqual(result, -1)
    
    def test_tuple(self):
        my_list = (3, 8)
        result = max_integer(my_list)
        self.assertEqual(result, 8)

    def test_elemnt_one(self):
        my_list = [1]
        result = max_integer(my_list)
        self.assertEqual(result, 1)

    def test_none(self):
        my_list = []
        result = max_integer(my_list)
        self.assertEqual(result, None)
    
    def test_string(self):
        result = max_integer('string')
        self.assertEqual(result, 't')

    def test_number(self):
        self.assertRaises(TypeError, max_integer, 1)

    def test_string_list(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "3", 4])

    def test_negative_number(self):
        self.assertRaises(TypeError, max_integer, -2)

if __name__ == '__main__':
    unittest.main()