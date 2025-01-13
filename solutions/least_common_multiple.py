#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the Least Common Multiple (LCM) of a list of three integers

Module contents:
    - least_common_multiple: function to calculates the LCM

Created on 12/01/2025
@author: Amin
"""


def least_common_multiple(nums: list) -> int:
    """calculate the Least Common Multiple for a list of three integers.

    Parameters:
        nums: list, the input list containing the three integers

    Returns -> int: the Least Common Multiple for the three integers
    Raises:
        AssertionError: if the argument is not a list
    Examples:
    >>> least_common_multiple([1, 2, 3])
    6
    >>> least_common_multiple([3, 4, 5])
    60
    >>> least_common_multiple([2, 1, 5])
    10
    """
    assert isinstance(nums, list), "input must be a list"
    # Check if the input list contains three elements
    if len(nums) != 3:
        return -1
    # Sort the input list of integers
    nums.sort()
    # Iterate through multiples of the greatest number (c) within a range up to the numbers product
    # Return the first multiple that is divisible by the other numbers (b, a)
    c = nums[2]
    b = nums[1]
    a = nums[0]
    for i in range(c, c * b * a + 1, c):
        if i % b == 0 and i % a == 0:
            return i
