"""
This is Lesson 33. Customizing classes
Get Programming: Learn to Code with Python
"""

class Fraction(object):
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __mul__(self, other_fraction):
        new_top = self.top * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        print(new_top, new_bottom)


fraction_1 = Fraction(1, 2)
fraction_2 = Fraction(4, 5)

fraction_1.__mul__(fraction_2)

# Now using the multiplication symbol also works on fractions
# The __mul__ method replaces the normal multiplication method
fraction_1 * fraction_2
