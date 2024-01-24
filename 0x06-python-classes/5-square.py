class Square:
    """
    This is a class that defines a square.
    Attributes: __size (int)
    """
    def __init__(self, size=0):
        """
        The constructor for the Square class.
        Parameters:
           size (int, optional): size of a side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        The getter method for size.
        Returns: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter method for size.
        Parameters:
           value (int): The size of a side of the square.
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
            int: The area of the current square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        The function to print the square with the character #.
        Prints an empty line if size is equal to 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
