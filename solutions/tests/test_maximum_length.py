#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for maximum_length function.

Test categories:
    - Standard cases: list of strings that may have unique or overlapping characters
    - Edge cases: empty lists, strings with identical bounds or duplicate characters, substrings with repetitive letters
    - Defensive tests: invalid inputs, assertions, or `TypeError` exceptions

Created on 2024-01-12
Author: Kefah Albashityalshaer
"""

import unittest

from ..maximum_length import max_length


class TestMaxLengthFunction(unittest.TestCase):
    # Standard test cases
    def test_basic_cases(self):
        self.assertEqual(
            max_length(["un", "iq", "ue"]), 4
        )  # "uniq" forms a concatenated string of length 4
        self.assertEqual(
            max_length(["cha", "r", "act", "ers"]), 6
        )  # The longest concatenated string is "acters" (length 6)
        self.assertEqual(
            max_length(["abcdefghijklmnopqrstuvwxyz"]), 26
        )  # The string contains all unique lowercase letters (length 26)

    # Edge Cases
    def test_empty_list(self):
        self.assertEqual(
            max_length([]), 0
        )  # No strings to concatenate, so the result is 0

    def test_single_element(self):
        self.assertEqual(max_length(["a"]), 1)
        self.assertEqual(max_length(["abcdef"]), 6)

    def test_no_unique_concatenation(self):
        self.assertEqual(max_length(["a", "bb", "ccc"]), 1)

    def test_repeated_characters(self):
        self.assertEqual(max_length(["abc", "def", "abc"]), 6)

    def test_large_input(self):
        arr = ["ab", "cd", "ef", "gh", "ij", "kl", "mnop"]
        self.assertEqual(max_length(arr), 16)  # Longest possible combination

    # Defensive tests
    def test_invalid_input(self):
        with self.assertRaises(
            AssertionError,
            msg="Input should raise an AssertionError for non-list input.",
        ):
            max_length("not a list")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            max_length(["abc", 123, "def"])

    def test_empty_strings(self):
        self.assertEqual(max_length(["", "abc", "de"]), 5)


if __name__ == "__main__":
    unittest.main()
