"""
This is Lesson 31. Creating a class for an object type
Get Programming: Learn to Code with Python
"""


class Circle(object):
    def __init__(self):
        self.radius = 4

    def get_area(self, radius):
        self.radius = radius
        area = 3.14 * radius**2
        return area


circle_one = Circle()
print(Circle.get_area(circle_one, 2))
