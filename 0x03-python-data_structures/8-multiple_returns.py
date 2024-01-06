#!/usr/bin/python3

def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)
    else:
        # Return a tuple with the length of the string and its first character
        return (len(sentence), sentence[0])

