#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None
    
    # Initialize max_value with the first element of the list
    max_value = my_list[0]

    # Iterate through the list to find the maximum value
    for elements in my_list:
        if elements > max_value:
            max_value = elements

    return max_value

