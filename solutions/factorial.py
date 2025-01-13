#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module contains afunction  to compute the factorial of a number

Module contents:
    -factorial: a function  to compute the factorial of a number

created on 9 Jan 2025
Author: Azza Ibrahim

"""


def factorial(number: int) -> int:
    """
    A function computes a factorial of a number

    parameters :
    Number (int) : the number to compute its factorial

    Return:
    int : THE fsctorial of the inpiut number

    Raises:
    ValueError: Factotial is only defined for positive numbers

    """
    if number == 0 or number == 1:
        return 1

    if number < 0:
        raise ValueError("Factotial is only defined for positive numbers")

    res = 1
    for f in range(2, number + 1):
        res *= f

    return res
