#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for j in range(len(str)):
        if j == n:
            continue
        else:
            new += str[j]
    return new
