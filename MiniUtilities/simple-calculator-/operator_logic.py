"""
operator_logic.py

This module defines the OperatorLogic class, which handles 
basic arithmetic operations such as addition, subtraction,
multiplication, and division.

Author: [Haashiraaa]
"""

import math
from functools import reduce
from operator import sub, truediv


class OperatorLogic:
    """
    A class that encapsulates core arithmetic operations.

    Methods
    -------
    add(n)
        Returns the sum of all numbers in the list `n`.
    subtract(n)
        Returns the result of sequential subtraction on elements in `n`.
    multiply(n)
        Returns the product of all numbers in the list `n`.
    divide(n)
        Returns the result of sequential division on elements in `n`.
    """

    def add(self, n):
        """Return the sum of numbers in the list `n`."""
        return sum(n)

    def subtract(self, n):
        """Return the result after sequential subtraction of list elements."""
        return reduce(sub, n)

    def multiply(self, n):
        """Return the product of numbers in the list `n`."""
        return math.prod(n)

    def divide(self, n):
        """
        Return the result after sequential division of list elements.
        Raises ZeroDivisionError if division by zero occurs.
        """
        return reduce(truediv, n)
