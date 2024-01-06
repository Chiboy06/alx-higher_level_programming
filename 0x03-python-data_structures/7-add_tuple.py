#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    #
    # Initialize the result tuple with two zeros
    result_tuple = (0, 0)
    # Loop through the first two indices
    for i in range(2):
        # Get the element from tuple_a or 0 if out of bounds
        a = tuple_a[i] if i < len(tuple_a) else 0
        # Get the element from tuple_b or 0 if out of bounds
        b = tuple_b[i] if i < len(tuple_b) else 0
        # Add the elements and update the result tuple
        result_tuple = result_tuple[:i] + (a + b,) + result_tuple[i+1:]
    # Return the result tuple
    return result_tuple
