#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_arguments = len(argv) - 1

    if num_arguments == 1:
        print(f"{num_arguments} argument:")
    elif num_arguments > 1:
        print(f"{num_arguments} arguments:")
    else:
        print(f"{num_arguments} arguments.")

    for i, arg in enumerate(argv[1:], start=1):
        print(f"{i}: {arg}")
