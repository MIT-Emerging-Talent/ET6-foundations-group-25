#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_number_odd funcion
contains test cases

Test cases:
    - vaild odd input
    - valid even input
    - vaild negative odd input
    - valid negative even input
    - empty iinput
    - float input
    -boolean input


created on 9 Jan 2026
Authon: Azza Ibrahim


"""

import unittest
from ..is_number_odd import is_number_odd


class TestIsNumberOdd(unittest.TestCase):
    """
    Test suite for the is_number_odd function.
    """

    def test_odd_int(self):
        """test case for a valid odd num"""
        self.assertTrue(is_number_odd(5))

    def test_even_num(self):
        """Test case for a valid even num"""
        self.assertFalse(is_number_odd(6))

    def test_zero(self):
        """test casefor zero"""
        self.assertFalse(is_number_odd(0))

    def test_neg_odd(self):
        "test case for negative input number"
        self.assertTrue(is_number_odd(-5))

    def test_neg_even(self):
        """Test case for negative even input"""
        self.assertFalse(is_number_odd(-4))

    def test_non_int(self):
        """test case for non integer input"""
        with self.assertRaises(AssertionError):
            is_number_odd("azza")

    def test_empty(self):
        """test case for empty input"""
        with self.assertRaises(ValueError):
            is_number_odd(None)

    def test_float(self):
        """Test case for float input"""
        with self.assertRaises(AssertionError):
            is_number_odd(5.5)

    def test_bool(self):
        """TEST case for bolean input"""
        with self.assertRaises(AssertionError):
            is_number_odd(True)
