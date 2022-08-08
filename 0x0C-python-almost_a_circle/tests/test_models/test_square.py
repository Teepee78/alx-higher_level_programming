#!/usr/bin/python3
"""This module defines unittests for Square.py"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Unittests for Square.py"""

    def test_init_none(self):
        """Test init method with no argument"""
        with self.assertRaises(TypeError):
            r1 = Square()

    def test_init_proper(self):
        """Test init method with proper arguments"""
        r1 = Square(2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Square(2, 4, 5, 6)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
        self.assertEqual(r2.id, 6)

    def test_init_errors(self):
        """Test init method raises appropriate errors"""
        with self.assertRaises(TypeError):
            r1 = Square("3")
        with self.assertRaises(TypeError):
            r1 = Square(3, "4")
        with self.assertRaises(TypeError):
            r1 = Square(3, 4, "5")
        with self.assertRaises(ValueError):
            r1 = Square(0)
        with self.assertRaises(ValueError):
            r1 = Square(3, -1, 0)
        with self.assertRaises(ValueError):
            r1 = Square(3, 0, -1)

    def test_str(self):
        """Test str method"""
        r1 = Square(3, 4, 5, 6)
        self.assertEqual(r1.__str__(), "[Square] (6) 4/5 - 3")

    def test_area(self):
        """Test area method"""
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)
        r2 = Square(4)
        self.assertEqual(r2.area(), 16)

    def test_display_xy(self):
        """Test display with x and y position"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Square(3, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ###\n  ###\n  ###\n")

    def test_display_0y(self):
        """Test display with x=0 and y position"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Square(2, 0, 1)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n##\n##\n")

    def test_display_x0(self):
        """Test display with x position and y=0"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Square(3, 1, 0)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ###\n ###\n ###\n")

    def test_update(self):
        """Tests update method"""
        r1 = Square(3)
        r1.update(1, 4)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 4)
        r2 = Square(2)
        r2.update(id=5, size=7)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.size, 7)

    def test_update_error(self):
        r2 = Square(2)
        """Test update with invalid attributes"""
        with self.assertRaises(AttributeError):
            r2.update(width=8)
            self.assertEqual(r2.weight, 8)
        with self.assertRaises(IndexError):
            r2.update(1, 2, 3, 4, 5, 6, 7)
            self.assertEqual(r2.id, 1)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Square(3, 4, 5, 6)
        dict1 = {
            "id": 6,
            "size": 3,
            "x": 4,
            "y": 5
        }
        self.assertIsInstance(r1.to_dictionary(), dict)
        self.assertEqual(r1.to_dictionary(), dict1)
