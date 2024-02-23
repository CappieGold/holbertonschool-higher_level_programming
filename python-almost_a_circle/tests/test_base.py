#!/usr/bin/python3
""" Unit tests for Base class """

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Contains multiple test cases for the Base class
    """

    def setUp(self):
        """
        Set up method to reset the private class attribute before each test
        """
        Base._Base__nb_objects = 0

    def test_01_id_auto_increment(self):
        """
        Test if id is automatically incremented when not provided
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_02_id_manual_assignment(self):
        """
        Test if manual id assignment works as expected
        """
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_03_mixed_id_assignment(self):
        """
        Test mixed automatic and manual id assignment
        """
        b4 = Base()
        b5 = Base(8)
        b6 = Base()
        b7 = Base(None)
        b8 = Base(5)

        self.assertEqual(b4.id, 1)
        self.assertEqual(b5.id, 8)
        self.assertEqual(b6.id, 2)
        self.assertEqual(b7.id, 3)
        self.assertEqual(b8.id, 5)

    def test_to_json_string_with_valid_dict(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_json = json.dumps([dictionary])
        self.assertEqual(json_dictionary, expected_json)
        self.assertIsInstance(json_dictionary, str)

    def test_to_json_string_with_empty_list(self):
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_with_none(self):
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_from_json_string_with_valid_json(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_with_empty_string(self):
        self.assertEqual(Rectangle.from_json_string(""), [])

    def test_from_json_string_with_none(self):
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_create_method(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(r1_dictionary, r2.to_dictionary())
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

class TestRectangleSaveToFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(10, 7, 2, 8)
        cls.r2 = Rectangle(2, 4)

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_with_objects(self):
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected = json.dumps([self.r1.to_dictionary(), self.r2.to_dictionary()])
            self.assertEqual(content, expected)

    def test_save_to_file_with_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

class TestLoadFromFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(10, 7, 2, 8)
        cls.r2 = Rectangle(2, 4)
        Rectangle.save_to_file([cls.r1, cls.r2])

        cls.s1 = Square(5)
        cls.s2 = Square(7, 9, 1)
        Square.save_to_file([cls.s1, cls.s2])


    def test_load_from_file_squares(self):
        list_squares = Square.load_from_file()
        self.assertEqual(len(list_squares), 2)
        self.assertIsInstance(list_squares[0], Square)
        self.assertIsInstance(list_squares[1], Square)
        self.assertNotEqual(id(list_squares[0]), id(self.s1))
        self.assertNotEqual(id(list_squares[1]), id(self.s2))

    def test_load_from_file_rectangles(self):
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles), 2)
        self.assertIsInstance(list_rectangles[0], Rectangle)
        self.assertIsInstance(list_rectangles[1], Rectangle)
        self.assertNotEqual(id(list_rectangles[0]), id(self.r1))
        self.assertNotEqual(id(list_rectangles[1]), id(self.r2))

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()
