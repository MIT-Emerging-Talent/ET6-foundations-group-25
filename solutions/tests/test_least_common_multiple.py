#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the least_common_multiple function.

Test cases include:
    - Valid inputs: a list of three integers.
    - Sorted and unsorted numbers.
    - Invalid inputs: a list of invalid range.
    - A list containing number formats other than integers.
    - Edge cases: special numbers such as 0 and negative numbers.

Created on 12/01/2025
@author: Amin
"""

import unittest

from ..least_common_multiple import least_common_multiple


class TestLeastCommonMultiple(unittest.TestCase):
    """Test the least_common_multiple function"""

    def test_sorted_list(self):
        """It should return the Least Common Multiple for a sorted list of three integers"""
        self.assertEqual(least_common_multiple([2, 3, 4]), 12)

    def test_unsorted_list(self):
        """It should return the Least Common Multiple for a sorted list of three integers"""
        self.assertEqual(least_common_multiple([5, 2, 4]), 20)

    def test_more_than_three_numbers(self):
        """It should return -1 for a list containing more than three integers"""
        self.assertEqual(least_common_multiple([1, 2, 3, 4]), -1)

    def test_fewer_than_three_numbers(self):
        """It should return -1 for a list containing fewer than three integers"""
        self.assertEqual(least_common_multiple([1, 2]), -1)

    def test_empty_list(self):
        """It should return -1 for an empty list"""
        self.assertEqual(least_common_multiple([]), -1)

    def test_including_zero(self):
        """It should return None for lists including 0"""
        self.assertEqual(least_common_multiple([0, 2, 4]), None)

    def test_including_negative_numbers(self):
        """It should return None for lists including 0"""
        self.assertEqual(least_common_multiple([-1, 9, 5]), None)

    def test_non_integer_numbers(self):
        """It should raise ValueError for lists containing numbers other than integers"""
        with self.assertRaises(TypeError):
            least_common_multiple([1.2, 5, 2])

    def test_not_list(self):
        """It should raise AssertionError for non-list inputs"""
        with self.assertRaises(AssertionError):
            least_common_multiple("not a list")
