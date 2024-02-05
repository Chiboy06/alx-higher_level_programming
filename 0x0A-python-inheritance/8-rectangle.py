#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle from BaseGeometry"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)

