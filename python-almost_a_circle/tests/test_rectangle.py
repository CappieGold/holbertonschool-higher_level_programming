#!/usr/bin/python3
""" Unit tests for Rectangle class """

import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Test class
    """

    def setUp(self):
        """Test"""
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width_height_type_validation(self):
        """test"""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_height_value_validation(self):
        """test"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_y_type_validation(self):
        """test"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0", 0)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0")

    def test_x_y_value_validation(self):
        """test"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """test"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """test"""
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
        """test"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_with_xy(self):
        """test"""
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

    def test_update(self):
        """test"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs_only(self):
        """test"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_kwargs(self):
        """test"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1, width=2, y=3, x=4, id=88)
        self.assertEqual(str(r1), "[Rectangle] (88) 4/3 - 2/1")

    def test_to_dictionary(self):
        """test"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        expected_dict = {'id': r1.id, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1_dict, expected_dict)
        self.assertIsInstance(r1_dict, dict)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        self.assertEqual(str(r2), str(r1))
        self.assertFalse(r1 == r2)

    def test_to_dictionary_with_varied_values(self):
        """test"""
        r1 = Rectangle(5, 7, 2, 8, 12)
        r1_dict = r1.to_dictionary()
        expected_dict = {'id': 12, 'width': 5, 'height': 7, 'x': 2, 'y': 8}
        self.assertEqual(r1_dict, expected_dict)

        r2 = Rectangle(3, 4, 1, 0, 10)
        r2_dict = r2.to_dictionary()
        expected_dict2 = {'id': 10, 'width': 3, 'height': 4, 'x': 1, 'y': 0}
        self.assertEqual(r2_dict, expected_dict2)

    def test_to_dictionary_independence(self):
        """test"""
        r1 = Rectangle(4, 2, 0, 0, 15)
        r1_dict = r1.to_dictionary()
        r1_dict['width'] = 10

        # Ensure original rectangle's width is unchanged
        self.assertEqual(r1.width, 4)

    def test_rectangle_missing_parameters(self):
        """test"""
        with self.assertRaises(TypeError):
            Rectangle(10)
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_edge_values(self):
        """test"""
        r = Rectangle(99999999, 99999999)
        self.assertEqual(r.width, 99999999)
        self.assertEqual(r.height, 99999999)

    def test_update_with_mixed_args(self):
        """test"""
        r = Rectangle(10, 10, 10, 10)
        r.update(12, height=2, y=3)
        self.assertEqual(str(r), "[Rectangle] (12) 10/3 - 10/2")

    def test_update_with_invalid_args(self):
        """test"""
        r = Rectangle(10, 10)
        with self.assertRaises(ValueError):
            r.update(width=-10)
        with self.assertRaises(TypeError):
            r.update(x="2")

    def test_state_after_update(self):
        """test"""
        r = Rectangle(10, 10)
        r.update(20, 30, 40, 50, 60)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 60)

    def test_rectangle_width_zero(self):
        """test"""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5, 0, 0)

    def test_rectangle_width_zero_with_id(self):
        """test"""
        with self.assertRaises(ValueError):
            Rectangle(0, 5, 0, 0, 10)

    def test_rectangle_set_width_to_zero(self):
        """test"""
        r = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_width_type_error(self):
        """test"""
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.width = "10"

    def test_width_negative_value_error(self):
        """test"""
        r = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_width_zero_value_error(self):
        """test"""
        r = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_width_type_error_on_creation(self):
        """test"""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_negative_value_error_on_creation(self):
        """test"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_width_zero_value_error_on_creation(self):
        """test"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)


if __name__ == "__main__":
    unittest.main()
