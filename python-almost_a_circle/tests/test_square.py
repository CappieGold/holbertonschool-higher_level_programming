#!/usr/bin/python3
"""test for class Square"""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    test
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        """test"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)

    def test_size_setter(self):
        """test"""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")

        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_update_method(self):
        """test"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary_square(self):
        """test"""
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': s1.id, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, expected_dict)
        self.assertIsInstance(s1_dict, dict)

        s2 = Square(1, 1)
        s2.update(**s1_dict)
        self.assertEqual(str(s2), str(s1))
        self.assertFalse(s1 == s2)

    def test_square_invalid_size(self):
        """test"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(TypeError):
            Square("5")

    def test_setters_with_invalid_values(self):
        """test"""
        s = Square(3)
        with self.assertRaises(ValueError):
            s.size = -10
        with self.assertRaises(TypeError):
            s.x = "2"
        with self.assertRaises(ValueError):
            s.y = -1

    def test_str_method(self):
        """test"""
        s = Square(4, 5, 6, 7)
        self.assertEqual(str(s), "[Square] (7) 5/6 - 4")

    def test_area_with_different_sizes(self):
        """test"""
        s = Square(2)
        self.assertEqual(s.area(), 4)
        s.size = 3
        self.assertEqual(s.area(), 9)

    def test_serialization_deserialization(self):
        """test"""
        s = Square(4, 5, 6, 7)
        s_dict = s.to_dictionary()
        new_s = Square.create(**s_dict)
        self.assertEqual(str(new_s), str(s))
        self.assertNotEqual(id(new_s), id(s))


if __name__ == "__main__":
    unittest.main()
