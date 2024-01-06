#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
    else:
        for row in matrix:
            for i, num in enumerate(row):
                if i == 0:
                    print("{:d}".format(num), end="")
                else:
                    print(" {:d}".format(num), end="")
            print("")

