#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module to check if the string is a Palindrome

A phrase is a `palindrome` if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Return `true` if it is a palindrome, or `false` otherwise.

Module contents:
    - isPalindrome: Given a string s, return true if it is a palindrome, or false otherwise

Created on 2024-01-12
Author: Kefah Albashityalshaer
"""


def isPalindrome(s: str) -> bool:
    """
    Function to find the `Palindrome`, which is a Alphanumeric characters that
    can be read the same forward and backward

    Takes a string with mix of Alphanumeric and non-alphanumeric, converting it to lowercase, removing
    all non-alphanumeric characters, and check if the result is `Palindrome`

    Parameters:
      s: str, s is a string to be checked if it's a Palindrome

    Return -> Bool: the return values is a boolean, True or False

    Examples:
    >>> isPalindrome("A man, a plan, a canal: Panama")
    True
    >>> isPalindrome("race a car")
    False
    >>> isPalindrome(" ")
    True
    """
    assert isinstance(s, str), "input should be a string"

    new_s = ""
    for char in s:
        if char.isalpha() or char.isnumeric():
            new_s += char.lower()
    return new_s == new_s[::-1]
