"""
Module providing arithmetic functions.

Provides functions for adding and multiplying numbers.

Functions:
    add(a, b): Returns the sum of two numbers.
    mult(a, b): Returns the product of two numbers.
"""


def hello():
    """Prints Hello message"""
    return 'Hello, CI World!'


def add(a, b):
    """Add two numbers"""
    return a + b


if __name__ == "__main__":
    print(hello())
    print(f"1 + 2 = {add(1, 2)}")
