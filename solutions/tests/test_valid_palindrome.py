#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for isPalindrome function in valid_palindrome.py

Test categories:
    - Standard cases: tests typical palindromes and tests typical non-palindromes
    - Edge cases: empty string, single character
    - Special tests: Ignores spaces, punctuation and handles numbers as palindromes

Created on 2024-01-12
Author: Kefah Albashityalshaer
"""

import unittest

from ..valid_palindrome import isPalindrome


class TestIsPalindromesFunction(unittest.TestCase):
    """Unit Test for the isPalindrome Function"""

    # Standard Test Cases (Palindromes and Non-Palindromes)
    def test_simple_palindrome(self):
        """Should return True for 'madam'"""
        self.assertTrue(isPalindrome("madam"))

    def test_simple_non_palindrome(self):
        """Should return False for 'hello'"""
        self.assertFalse(isPalindrome("hello"))

    # Edge Cases
    def test_empty_string(self):
        """Should return True for an empty string"""
        self.assertTrue(isPalindrome(""))

    def test_single_character(self):
        """Should return True for a single character"""
        self.assertTrue(isPalindrome("a"))

    def test_mixed_case(self):
        """Should return True regardless of case"""
        self.assertTrue(isPalindrome("MadAm"))

    # Special Cases
    def test_special_characters(self):
        """Should return True ignoring special characters"""
        self.assertTrue(isPalindrome("A man, a plan, a canal: Panama"))

    def test_numeric_palindrome(self):
        """Should return True for numeric palindrome"""
        self.assertTrue(isPalindrome("12321"))

    def test_mixed_alpha_numeric(self):
        """Should return True for alphanumeric palindrome"""
        self.assertTrue(isPalindrome("1a2b2a1"))


if __name__ == "__main__":
    unittest.main()
