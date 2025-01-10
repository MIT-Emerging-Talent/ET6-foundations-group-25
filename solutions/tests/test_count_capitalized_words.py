#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the count_capitalized_words function.

Test cases include:
    - Strings with capitalized words.
    - Strings without capitalized words.
    - Edge cases: empty strings, single-character strings, strings with mixed cases.
    - Invalid inputs: non-string values (e.g., integers or floats).

Created on 05/01/2025
@author: Amin
"""

import unittest

from ..count_capitalized_words import count_capitalized_words


class TestCountCapitalizedWords(unittest.TestCase):
    """Test the count_capitalized_words function"""

    def test_empty_string(self):
        """It should return 0 for an empty string"""
        self.assertEqual(count_capitalized_words(""), 0)

    def test_single_uppercase_character_string(self):
        """It should return 1 for a string that contain a single uppercase character"""
        self.assertEqual(count_capitalized_words("A"), 1)

    def test_no_uppercase(self):
        """It should return 0 for strings without words starting with uppercase"""
        self.assertEqual(count_capitalized_words("yes"), 0)

    def test_all_capitalized(self):
        """It should count all the words in the string"""
        self.assertEqual(count_capitalized_words("A Capitalized Sentence"), 3)

    def test_mixed_case(self):
        """It should handle strings with words of mixed characters"""
        self.assertEqual(count_capitalized_words("Happy new year"), 1)

    def test_uppercase_not_the_first_letter(self):
        """It should return 0 if there is and uppercase but not as the first letter of a word"""
        self.assertEqual(count_capitalized_words("this is an eXample"), 0)

    def test_not_string(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            count_capitalized_words(101)
