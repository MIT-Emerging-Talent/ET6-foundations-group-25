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
    # Standard Test Cases (Palindromes and Non-Palindromes)
    def test_simple_palindrome(self):
        self.assertTrue(isPalindrome("madam"), "Should return True for 'madam'")
        self.assertTrue(isPalindrome("racecar"), "Should return True for 'racecar'")

    def test_simple_non_palindrome(self):
        self.assertFalse(isPalindrome("hello"), "Should return False for 'hello'")
        self.assertFalse(isPalindrome("world"), "Should return False for 'world'")

    # Edge Cases
    def test_empty_string(self):
        self.assertTrue(isPalindrome(""), "Should return True for an empty string")

    def test_single_character(self):
        self.assertTrue(isPalindrome("a"), "Should return True for a single character")

    def test_mixed_case(self):
        self.assertTrue(isPalindrome("MadAm"), "Should return True regardless of case")
        self.assertTrue(
            isPalindrome("RaCeCaR"), "Should return True regardless of case"
        )

    # Special Cases
    def test_special_characters(self):
        self.assertTrue(
            isPalindrome("A man, a plan, a canal: Panama"),
            "Should return True ignoring special characters",
        )
        self.assertTrue(
            isPalindrome("No lemon, no melon!"),
            "Should return True ignoring punctuation",
        )

    def test_numeric_palindrome(self):
        self.assertTrue(
            isPalindrome("12321"), "Should return True for numeric palindrome"
        )
        self.assertFalse(
            isPalindrome("12345"),
            "Should return False for non-palindrome numbers",
        )

    def test_mixed_alpha_numeric(self):
        self.assertTrue(
            isPalindrome("1a2b2a1"),
            "Should return True for alphanumeric palindrome",
        )
        self.assertFalse(
            isPalindrome("1a2b3c"),
            "Should return False for non-palindrome alphanumeric string",
        )


if __name__ == "__main__":
    unittest.main()
