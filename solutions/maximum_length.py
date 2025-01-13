#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module to find the maximum length of the
concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s

Module contents:
    - maxLength: Function to get the Maximum Length of a Concatenated String with Unique Characters
    - backtrack: Helper function to perform backtracking

Created on 2024-01-12
Author: Kefah Albashityalshaer
"""


def max_length(arr: list) -> int:
    """
    Function to get the Maximum Length of a Concatenated String with Unique Characters

    Takes a list of strings and returns the max length of concatenated string with unique characters

    Parameters:
        arr: list of stings elements to process

    Returns -> int: the maximum length

    Examples:
    >>> max_length(["un","iq","ue"])
    4
    >>> max_length(["cha","r","act","ers"])
    6
    >>> max_length(["abcdefghijklmnopqrstuvwxyz"])
    26
    >>> max_length(["a", "bb", "ccc"])
    1
    >>> max_length([])
    0
    """
    assert isinstance(arr, list), "input should be a list of strings"

    # Helper function to perform backtracking
    def backtrack(index, current_string):
        # If the current string has duplicate characters, return 0
        if len(current_string) != len(set(current_string)):
            return 0

        # Calculate the maximum length by trying to add each subsequent string
        max_length = len(current_string)
        for i in range(index, len(arr)):
            max_length = max(max_length, backtrack(i + 1, current_string + arr[i]))
        return max_length

    # Start the backtracking from index 0 and an empty string
    return backtrack(0, "")
