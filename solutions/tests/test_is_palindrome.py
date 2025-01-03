#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the is_palindrome function.

Test cases include:
    - Valid palindromes: strings that are palindromes.
    - Invalid palindromes: strings that are not palindromes.
    - Edge cases: empty strings, single-character strings, strings with mixed cases or spaces.
    - Invalid inputs: non-string values (e.g., integers or floats).

Created on 2024-01-01
@author: Alexander Andom
"""

import unittest

from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test the is_palindrome function"""

    def test_valid_palindrome_1(self):
        """It should return True"""
        result = is_palindrome("madam")
        self.assertTrue(result)

    def test_valid_palindrome_2(self):
        """It should return True"""
        result = is_palindrome("racecar")
        self.assertTrue(result)

    def test_valid_palindrome_3(self):
        """This is should return True"""
        result = is_palindrome("A man a plan a canal Panama")
        self.assertTrue(result)

    def test_invalid_palindrome(self):
        """It should return False"""
        result = is_palindrome("hello")
        self.assertFalse(result)

    def test_edge_case_empty_string(self):
        """It should return True"""
        result = is_palindrome("")
        self.assertTrue(result)

    def test_edge_case_single_character(self):
        """It should return True"""
        result = is_palindrome("a")
        self.assertTrue(result)

    def test_edge_case_spaces(self):
        """It should return True)"""
        result = is_palindrome("a b c b a")
        self.assertTrue(result)

    def test_edge_case_mixed_case(self):
        """It should return True"""
        result = is_palindrome("MadAm")
        self.assertTrue(result)

    def test_non_palindrome_mixed_characters(self):
        """Test for non-palindrome with mixed characters"""
        self.assertFalse(is_palindrome("Hello, world!"))

    def test_invalid_input_integer(self):
        """This should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            is_palindrome(12321)

    def test_invalid_input_float(self):
        """This should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            is_palindrome(123.21)


if __name__ == "__main__":
    unittest.main()
