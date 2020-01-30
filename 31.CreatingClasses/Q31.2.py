"""
This is Lesson 31. Creating a class for an object type
Get Programming: Learn to Code with Python
"""


class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area

    def get_perimiter(self):
        perimiter = (2 * self.length) + (2 * self.width)
        return perimiter


rectangle_one = Rectangle(2, 5)

# Print area and perimiter for rectangle_one, an instance of the Rectangle class
print(Rectangle.get_area(rectangle_one))
print(Rectangle.get_perimiter(rectangle_one))
