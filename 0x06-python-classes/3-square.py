#!/usr/bin/python3
class Square:
    """Defines a square"""
    def __init__(self, size = 0):
        """Initialises Data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        The function to calculate the area of the square.
        Returns:
            int:The current square area
        """
        return self.__size * self.__size
