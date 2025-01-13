#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for obtaining min integer from a list.

Module contents:
    - min_integer: Returns minimum integer from a list of integers

Created on 2025-01-09
Author: Tamir Elwaleeed
"""


def min_integer(my_list: list) -> int:
    """Returns the min integer in a list of integers
        If the list is empty, the function returns None

    Parameters:
        my_list: list, the list to find the min from

    Returns -> int: the min integer from the list

    Raises:
        AssertionError: if input is not a list

    Examples:
        >>> min_integer([1, 2, 3, 4, 5])
        1
        >>> min_integer([-1, -4, -5])
        -5
        >>> min_integer([])
        None
    """
    assert isinstance(my_list, list), "input must be a list"

    if len(my_list) == 0:
        return None
    result = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] < result:
            result = my_list[i]
        i += 1
    return result
