#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the words that begin with a capital letter (an uppercase letter) in a string.

Module contents:
    - count_capitalized_words: counts the words that begin with an uppercase letter in a string.

Created on 05/01/2025
@author: Amin
"""


def count_capitalized_words(text: str) -> int:
    """Count the number of words that begin with an uppercase letter in a string.

    Parameters:
        text: str, the input string to check

    Returns -> int: the number of words beginning with a capital letter in the text

    Raises:
        AssertionError: if the argument is not a string

    >>> count_capitalized_words("word")
    0
    >>> count_capitalized_words("One more")
    1
    >>> count_capitalized_words("A B C")
    3
    """
    assert isinstance(text, str), "input must be a string"

    count = 0
    # Transform the original text into a list by splitting it
    words = text.split()
    # Loop through each element and count the capitalized words by checking the first letter
    for i in words:
        if i[0] == i[0].upper():
            count += 1
    return count
