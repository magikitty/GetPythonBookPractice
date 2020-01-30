"""
This is Lesson 31. Creating a class for an object type
Get Programming: Learn to Code with Python
"""


class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width


a = Rectangle(1, 1)
b = Rectangle(1, 1)

# Calling methods using the instance name
a.set_height(4)
b.set_width(4)

# Calling methods using the dot notation on the class name
Rectangle.set_height(a, 4)
Rectangle.set_width(b, 4)
