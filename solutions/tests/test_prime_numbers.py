#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for prime_numbers function.
Checks if the given number is a prime number.

Test categories:
    - Standard cases: typical integer inputs.
    - Edge cases: special numbers such as 0 and 1.
    - Defensive tests: invalid inputs.

Created on 2025-01-04
Author: Alaa Mohamed
"""

import unittest

from ..prime_numbers import prime_numbers


class TestPrimeNumbers(unittest.TestCase):
    """

    Test case for the prime_numbers function.

    """


def test_not_int(self):
    """It should raise AssertionError for non-integer input"""
    with self.assertRaises(AssertionError):
        prime_numbers(1.5)


def test_edge_case(self):
    """Testing the function with edge inputs"""
    self.assertFalse(prime_numbers(1))


def test_negative_numbers(self):
    """Testing the function with negative inputs"""
    self.AssertFalse(prime_numbers(-5))


def test_large_prime_numbers(self):
    """Testing the function with large prime numbers"""
    self.assertTrue(prime_numbers(7919))


def test_large_non_prime_numbers(self):
    """Testing the function with large non-prime numbers"""
    self.assertFalse(prime_numbers(100000))
