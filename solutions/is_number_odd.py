#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A Module for determining whether a number is odd

Module contents:
    - is_number_odd : determine if the number is odd or not

created on 08/01/2025
@author: Azza Ibrahim



"""


def is_number_odd(number: int) -> bool:
    """
    The function takes an intger input from the user, validate the input,
    and determine if the number is odd, if the input is not an intger,
    an error is raised.

    Parameters:
        number: the intger to be determined whether odd or not

    Return:
        bool:
        True: if he number is odd
        False: if the number is not

    Raises:
        AssertionError: if the input is not an int
        ValueError: if the input is empty

    Exmples:
        >>> is_number_odd(3)
        True
        >>> is_number_odd(2)
        False
        >>> is_number_odd()
        Input cannot be empty
        >>> is_number_odd(sss)
        Input must be an intger

    """
    if number is None:
        raise ValueError("Input cannot be empty")
    if isinstance(number, bool):
        raise AssertionError("Input must be an integer, not a boolean")
    assert isinstance(number, int), "Input must be an integer"
    return number % 2 != 0
   

