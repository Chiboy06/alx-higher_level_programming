#!/usr/bin/python3
class Square:
    """
    Defines a square.
    Attributes: __size (int): size of a side of a square.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.
        Initialises the data.
        """
        return self.__size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter method for size.

        Parameters:
           int: The size of a side of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        The function to calculate the area of the square.
        Returns:
            int:Returns the current square area
        """
        return self.__size * self.__size
