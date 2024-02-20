#!/usr/bin/python3
""" Unit tests for Rectangle class """

import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width_height_type_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_height_value_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_y_type_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0", 0)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0")

    def test_x_y_value_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        r1 = Rectangle(4, 6)
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        self.assertEqual(s, "####\n####\n####\n####\n####\n####\n")

        r2 = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        s = f.getvalue()
        self.assertEqual(s, "##\n##\n")

    def test_str_method(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_with_xy(self):
        r1 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        s = f.getvalue()
        expected_output = " ###\n ###\n"
        self.assertEqual(s, expected_output)


if __name__ == "__main__":
    unittest.main()
