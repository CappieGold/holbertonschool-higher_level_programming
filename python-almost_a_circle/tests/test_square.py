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


if __name__ == "__main__":
    unittest.main()
