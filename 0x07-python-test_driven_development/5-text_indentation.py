#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in "?:.":
        text = (delimiter + "\n\n").join(
                [line.strip(" ") for line in text.split(delimiter)])

    print(text)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
