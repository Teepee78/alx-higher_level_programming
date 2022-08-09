#!/usr/bin/python3
"""This module defines unittests for base.py"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Unittests for base.py"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        """Initialize with no arguments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_init_param(self):
        """Initialize with arguments"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(25)
        self.assertEqual(b2.id, 25)
        b3 = Base(-1)
        self.assertEqual(b3.id, -1)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)

    def test_init_mix(self):
        """Mix init with ID and without"""
        b1 = Base(2)
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base(4)
        self.assertEqual(b3.id, 4)
        b4 = Base()
        self.assertEqual(b4.id, 2)

    def test_init_too_many(self):
        """Initialize with too many arguments"""
        with self.assertRaises(TypeError):
            b1 = Base(2, 3)

    def test_to_json_string(self):
        """Tests to_json_string method"""
        b1 = Base()
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        dic = [{'name': 'abbey'}]
        self.assertEqual(b1.to_json_string(dic), '[{"name": "abbey"}]')

    def test_from_json_string(self):
        """Tests from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        dic = [{'name': 'abbey'}]
        self.assertEqual(Base.from_json_string('[{"name": "abbey"}]'), dic)

    def test_create(self):
        """Test create method"""
        dic = {
            "id": 14,
            "x": 0,
            "y": 0,
            "width": 3,
            "height": 5
        }
        self.assertIsInstance(Rectangle.create(**dic), Rectangle)
        dic_1 = {
            "id": 13,
            "x": 0,
            "y": 0,
            "size": 3,
        }
        self.assertIsInstance(Square.create(**dic), Square)

    def test_save_to_file(self):
        """Test save_to_file method"""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            bases = json.load(f)
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            bases = json.load(f)
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])

    def test_load_from_file(self):
        """Test load_from_file with non-existant file"""
        obj = Base.load_from_file()
        self.assertEqual(obj, [])

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_file_csv_none(self):
        """Test save None object to csv file"""
        Rectangle.save_to_file_csv(None)
        with open("Base.csv", "r", newline='') as f:
            bases = Rectangle.load_from_file_csv()
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])

    def test_save_file_csv_empty(self):
        """Test save empty list to csv file"""
        Rectangle.save_to_file_csv([])
        with open("Base.csv", "r", newline='') as f:
            bases = Base.load_from_file_csv()
            self.assertEqual(len(bases), 0)
            self.assertEqual(bases, [])

    def test_load_from_file_csv(self):
        """Test loading non-existant file"""
        obj = Rectangle.load_from_file_csv()
        self.assertEqual(obj, [])
