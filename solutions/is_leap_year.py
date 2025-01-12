#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining if a year is a leap year.

Module contents:
    - is_leap_year(year): Determines if a year is a leap year.

Leap year rules:
    - A year is a leap year if it is divisible by 4.
    - However, years divisible by 100 are not leap years , unless it is divisible by 400.

Created on 2025-01-01
@author: Alexander Andom
"""


def is_leap_year(year: int) -> bool:
    """Check if a given year is a leap year.

    Parameters:
        year : int, The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Raises:
        AssertionError:
            - If 'year' is not an integer.
            - If 'year' is less than 1583.

    Example:
        >>> is_leap_year(2000)
        True

        >>> is_leap_year(1900)
        False

        >>> is_leap_year(2024)
        True
    """

    assert isinstance(year, int), "year must be an integer"
    assert year >= 1583, (
        "year must be greater than or equal to 1583 (1582 is start of Gregorian Calendar)"
    )

    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
