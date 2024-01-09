#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""

def add_integer(a, b=98):
    """Return the addition of two numbers."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Casting to integers if they are float
    a = int(a) if type(a) is float else int(a)
    b = int(b) if type(b) is float else int(b)

    return a + b
