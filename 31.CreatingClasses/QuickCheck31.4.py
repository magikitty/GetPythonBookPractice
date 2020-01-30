"""
This is Lesson 31. Creating a class for an object type
Get Programming: Learn to Code with Python
"""


class Door(object):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.open = False

    def change_state(self):
        self.open = not self.open

    def scale_door(self, factor):
        self.height *= factor
        self.width *= factor


square_door = Door()
square_door.change_state()
square_door.scale_door(3)
