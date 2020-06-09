#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Args:
        unittest ([type]): [description]
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base(self):
        base_1 = Base()
        self.assertIsInstance(base_1, Base)

    def test_base_not_id(self):
        base_2 = Base()
        self.assertEqual(base_2.id, 1)
        base_3 = Base()
        self.assertEqual(base_3.id, 2)

    def test_base_id(self):
        base_4 = Base(6)
        self.assertEqual(base_4.id, 6)

    def test_base_to_json_string_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

        empty_dictionary = Base.to_json_string([])
        self.assertIsInstance(empty_dictionary, str)
        self.assertEqual(empty_dictionary, '[]')

        none_dic = Base.to_json_string(None)
        self.assertEqual(none_dic, "[]")

        list_test = Base.from_json_string(json_dictionary)
        self.assertIsInstance(list_test, list)
        self.assertEqual(list_test[0]['width'], dictionary['width'])
        self.assertEqual(list_test[0]['height'], dictionary['height'])
        self.assertEqual(list_test[0]['x'], dictionary['x'])
        self.assertEqual(list_test[0]['y'], dictionary['y'])
        self.assertEqual(list_test[0]['id'], dictionary['id'])

    def test_base_to_and_from_json_string_square(self):
        r1 = Square(6, 6, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

        empty_dictionary = Base.to_json_string([])
        self.assertIsInstance(empty_dictionary, str)
        self.assertEqual(empty_dictionary, '[]')

        none_dic = Base.to_json_string(None)
        self.assertEqual(none_dic, "[]")

        list_test = Base.from_json_string(json_dictionary)
        self.assertIsInstance(list_test, list)
        self.assertEqual(list_test[0]['size'], dictionary['size'])
        self.assertEqual(list_test[0]['x'], dictionary['x'])
        self.assertEqual(list_test[0]['y'], dictionary['y'])
        self.assertEqual(list_test[0]['id'], dictionary['id'])

    def test_base_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        test_string = r2.__str__()
        self.assertEqual(test_string, "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)

    def test_base_create_square(self):
        r1 = Square(5, 3, 0)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)

        test_string = r2.__str__()
        self.assertEqual(test_string, "[Square] (1) 3/0 - 5")
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)


if __name__ == '__main__':
    unittest.main()
