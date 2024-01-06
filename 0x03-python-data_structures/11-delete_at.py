#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the index is valid
    if 0 <= idx < len(my_list):
        # Use del to remove the item at the index
        del my_list[idx]
    # Return the modified list
    return my_list

