"""
This is Lesson 31. Creating a class for an object type
Get Programming: Learn to Code with Python
"""

class Door(object):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.open = False


    def doorIsOpen(self):
        return self.open


    def doorArea(self):
        area = self.width * self.height
        return area
