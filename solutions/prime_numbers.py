#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A module that determines whether a given number is a prime number.

Module contents:
    - prime_numbers: checks if the given number is a prime number.

created on 04/01/2025
@author: Alaa Mohamed

"""


def prime_numbers(number: int) -> bool:
    """
    Checks if the given number is a prime number.
    A number is considered prime if it's only divisible by one and itself.


    Parameters:
        number: input must be an integer.

    Returns -> bool: True if the number is prime, False otherwise.

    Raises:
        AssertionError: if the input is not an integer.

    Examples:
    >>> prime_numbers(1)
    False
    >>> prime_numbers(2)
    True
    >>> prime_numbers(3)
    True
    """
    assert isinstance(number, int), "input must be an integer"

    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
