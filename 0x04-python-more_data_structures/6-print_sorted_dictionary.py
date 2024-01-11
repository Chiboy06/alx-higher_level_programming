def print_sorted_dictionary(a_dictionary):
    # Iterate over the keys in sorted order
    for key in sorted(a_dictionary.keys()):
        # Print the key and its corresponding value
        print("{}: {}".format(key, a_dictionary[key]))

