#!/usr/bin/python3
"""
    3-say_my_name Module
"""
def say_my_name(first_name, last_name=""):
    """
    Prints a message with the given first and last names.

    Args:
        first_name (str): First name.
        last_name (str): Last name.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name + " " + last_name
    print("My name is {}".format(full_name))
