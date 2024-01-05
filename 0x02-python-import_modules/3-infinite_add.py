#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_arguments = len(argv) - 1
    total = sum(int(arg) for arg in argv[1:]) if num_arguments > 0 else 0
    print(total)

