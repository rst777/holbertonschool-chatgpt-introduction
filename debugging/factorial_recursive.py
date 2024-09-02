#!/usr/bin/python3
"""
    Compute the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the integer n. If n is 0, returns 1.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> factorial(4)
        24
        >>> factorial(0)
        1
"""
import sys

def factorial(n):


        if n == 0:

                return 1

        else:
            return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)


