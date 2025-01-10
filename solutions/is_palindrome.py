#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a string is a palindrome.

A palindrome is a string that reads the same forwards and backwards,ignoring case and spaces.

Module contents:
    - is_palindrome(s): checks if a string is a palindrome.

Created on 2024-01-01
@author: Alexander Andom
"""


def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome.

    Parameters:
        s : str, The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        AssertionError: If the input is not a string.

    Examples:
        >>> is_palindrome('madam')
        True

        >>> is_palindrome('A man a plan a canal Panama')
        True

        >>> is_palindrome('hello')
        False
    """

    assert isinstance(s, str), "Input must be a string."

    s = s.replace(" ", "").lower()
    return s == s[::-1]
