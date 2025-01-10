#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Test module for missing_number function.
Checks with numbers are missed out of a sequence.

Test categories:
    - Standard cases: only one missing value.
    - Edge cases: empty list and list with one number.
    - Defensive tests: invalid inputs or duplicate values.

    Created on 2025-01-04
    Author: Alaa Mohamed

"""

import unittest

from ..missing_number import missing_number


class TestMissingNumber(unittest.TestCase):
    """Test case for missing_number foundation"""

    def test_only_one_missing_number(self):
        """The list is [0, 1, 3] and n is 3
        Missing number should be [2]"""
        self.assertEqual(missing_number([0, 1, 3], 3), [2])

    def test_an_empty_list(self):
        """The list is [] and n is 0
        Missing number should be [0]"""
        self.assertEqual(missing_number([], 0), [0])

    def test_list_with_one_number(self):
        """The list is [0] and n is 1
        Missing number should be [1]"""
        self.assertEqual(missing_number([0], 1), [1])

    def test_with_two_missing_numbers(self):
        """The list is [1, 3, 5] and n is 5
        Missing number should be [2, 4]"""
        self.assertEqual(missing_number([1, 3, 5], 5), [0, 2, 4])

    def test_list_with_no_missing_number(self):
        """The list is [0, 1, 2] and n is 2
        Missing number should be []"""
        self.assertEqual(missing_number([0, 1, 2], 2), [])

    def test_duplicate_numbers(self):
        """The list is [0, 1, 2, 2, 3, 4] and n is 4
        Missing number should be []"""
        self.assertEqual(missing_number([0, 1, 2, 2, 3, 4], 4), [])

    def test_invalid_input(self):
        """It should raise an assertion error if the input is invalid."""
        with self.assertRaises(AssertionError):
            missing_number([], 1.5)
