#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class testMaxInteger(unittest.TestCase):
    """
    Class for testing max_integer
    """
    def test_moduleDocstring(self):
        """
        Test module docstring
        """
        self.assertTrue(len(__import__('6-max_integer').__doc__) >= 1)

    def test_functionDocstring(self):
        """
        Test function docstring
        """
        self.assertTrue(len(max_integer.__doc__) >= 1)

    def test_isList(self):
        """
        Test if input is a list
        """
        x = [1, 2, 3]
        self.assertTrue(type(x) is list)

    def test_emptyList(self):
        """
        Test empty list
        """
        x = []
        self.assertIsNone(max_integer(x), "Empty list")

    def test_oneElement(self):
        """
        Test one element
        """
        x = [1]
        self.assertEqual(max_integer(x), 1)
   
    def test_maxInt(self):
        """
        Test max integer
        """
        x = [1, 2, 3, 4]
        self.assertEqual(max_integer(x), 4)
    
    def test_maxNegative(self):
        """
        Test max negative
        """
        x = [-1, -2, -4, -3]
        self.assertEqual(max_integer(x), -1)

    def test_maxFloat(self):
        """
        Test max float
        """
        x = [1.5, 2.5, 3.5, 4.5]
        self.assertEqual(max_integer(x), 4.5)
    
    def test_nonInt(self):
        """
        Test non integer
        """
        x = [1, 2, "3", 4]
        with self.assertRaises(TypeError):
            max_integer(x)
    
    def test_noArgs(self):
        """
        Test no arguments
        """
        self.assertIsNone(max_integer(), "No arguments")
   
    def test_None(self):
        """
        Test None
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_maxAtBeginning(self):
        """
        Test max at beginning
        """
        x = [4, 2, 3, 1]
        self.assertEqual(max_integer(x), 4)
    
    def test_MaxAtMiddle(self):
        """
        Test max at middle
        """
        x = [1, 2, 4, 3, 2]
        self.assertEqual(max_integer(x), 4)
    
    def test_oneNegative(self):
        """
        Test one negative
        """
        x = [-1,5,6,7]
        self.assertEqual(max_integer(x), 7)


if __name__ == '__main__':
    unittest.main()
        