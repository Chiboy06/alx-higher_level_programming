#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    
    reversed_list = my_list[::-1]
    
    for num in reversed_list:
        print("{:d}".format(num))

