def best_score(a_dictionary):
    # If the dictionary is not empty, return the key with the biggest value
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    # If the dictionary is empty, return None
    else:
        return None
