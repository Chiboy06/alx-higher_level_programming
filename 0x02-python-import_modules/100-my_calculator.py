#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    count = len(argv)

    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = {'+': add, '-': sub, '*': mul, '/': div}
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
