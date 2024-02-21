#!/usr/bin/python3
""" Unit tests for Base class """

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


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

if __name__ == "__main__":
    unittest.main()
