#!/usr/bin/python3

"""Unittests for base.py"""

from unittest.mock import patch
from unittest import TestCase
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(TestCase):
    """ Base class tests"""

    def setUp(self):
        """ Resets nb_objects to 0 """
        Base._Base__nb_objects = 0
    
    def test_id(self):
        """ tests id : default and custom """
        # default
        new1 = Base()
        new2 = Base()
        # custom
        new3 = Base(3)
        # default
        new4 = Base()
        # custom negative zero, string, list, dict, tuple, None, float
        new6 = Base(-5)
        new7 = Base(0)
        new8 = Base(8.5)
        new9 = Base("string")
        new10 = Base([1, 2, 3])
        new11 = Base({"a": 1, "new": 2})
        new12 = Base((1, 2, 3))
        new13 = Base(None)
        new14 = Base(float('inf'))
        new15 = Base(float('NaN'))
        new16 = Base(float('-inf'))
        new17 = Base(float('1.5'))
        new18 = Base(float('-1.5'))

        self.assertEqual(new1.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)
        self.assertEqual(new4.id, 3)
        self.assertEqual(new6.id, -5)
        self.assertEqual(new7.id, 0)
        self.assertEqual(new8.id, 8.5)
        self.assertEqual(new9.id, "string")
        self.assertEqual(new10.id, [1, 2, 3])
        self.assertEqual(new11.id, {"a": 1, "new": 2})
        self.assertEqual(new12.id, (1, 2, 3))
        self.assertEqual(new13.id, 1)
        self.assertEqual(new14.id, float('inf'))
        self.assertEqual(new15.id, float('NaN'))
        self.assertEqual(new16.id, float('-inf'))
        self.assertEqual(new17.id, float('1.5'))
        self.assertEqual(new18.id, float('-1.5'))

    def test_more_than_one_arg(self):
        """ tests more than one arg """
        with self.assertRaises(TypeError):
            Base(1, 2)
    
    def test_nb_objects(self):
        """ tests nb_objects """
        new1 = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new1.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_save_to_file_rect(self):
        """ test JSON string to file """
        # test empty list
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        # test None
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
    
    def test_save_to_file_square(self):
        """ test JSON string to file """
        # test empty list
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        # test None
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_access_privateatt(self):
        """ test access  to private attribute """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
