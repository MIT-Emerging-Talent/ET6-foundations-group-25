#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for min_integer function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements, strings
    - Defensive tests: wrong input types, assertions

Created on 2025-01-09
Author: Tamir Elwaleeed
"""

import unittest
from ..min_integer import min_integer


class TestMinInteger(unittest.TestCase):
    """Define unittests for min_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(min_integer(ordered), 1)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(min_integer(unordered), 1)

    def test_min_at_beginning(self):
        """Test a list with a beginning min value."""
        min_at_beginning = [1, 4, 3, 2]
        self.assertEqual(min_integer(min_at_beginning), 1)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(min_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(min_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(min_integer(floats), -9.123)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(min_integer(ints_and_floats), -9)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        with self.assertRaises(AssertionError):
            min_integer(string)

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(min_integer(strings), "Brennan")

    def test_empty_string(self):
        """Test an empty string."""
        with self.assertRaises(AssertionError):
            min_integer("")


if __name__ == "__main__":
    unittest.main()
