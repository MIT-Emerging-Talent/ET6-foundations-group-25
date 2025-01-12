#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module contain test cases for factorial function

Test categories:
        normal cases
        bounry cases
        defensice assertaion


created on 12 Jan 2025
Author: Azza Ibrahim
"""

import unittest
from ..factorial import factorial


class TestFactorial(unittest.TestCase):
    """
    Class contiain unit tests for factorial function
    """

    def test_factorial_positive(self):
        """test factorial for a positive input number"""
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        """TEst factorial functipn fo input of zero"""
        self.assertEqual(factorial(0), 1)

    def test_factorail_one(self):
        """test factorial for input one"""
        self.assertEqual(factorial(1), 1)

    def test_factorail_large(self):
        """test factorail for large input number"""
        self.assertEqual(factorail(11), 39916800)

    def test_negative(self):
        """test negative input will raise error"""
        with self.assertRaises(ValueError):
            factorail(-3)

    def test_non_intger(self):
        """test case for non intger input"""
        with self.assertRaises(TypeError):
            factorial(5.5)


if __name__ == "__main__":
    unittest.main()
