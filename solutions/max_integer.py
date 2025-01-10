#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for obtaining max integer from a list.

Module contents:
    - max_integer: Returns maximum integer from a list of integers

Created on 2025-01-08
Author: Tamir Elwaleeed
"""


def max_integer(my_list: list) -> int:
    """Returns the max integer in a list of integers
        If the list is empty, the function returns None

    Parameters:
        my_list: list, the list to find the max from

    Returns -> int: the max integer from the list

    Raises:
        AssertionError: if input is not a list
        AssertionError: if one of the elements isn't a number

    Examples:
        >>> max_integer([1, 2, 3, 4, 5])
        5
        >>> max_integer([-1, -4, -5])
        -1
        >>> max_integer([])
        None
    """
    assert isinstance(my_list, list), "input must be a list"

    if len(my_list) == 0:
        return None
    result = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > result:
            result = my_list[i]
        i += 1
    return result
