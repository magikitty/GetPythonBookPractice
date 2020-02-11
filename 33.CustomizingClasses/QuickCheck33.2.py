"""
This is Lesson 33. Customizing classes
Get Programming: Learn to Code with Python
"""

# Quick Check 33.2
class Fraction(object):
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __mul__(self, other_fraction):
        new_top = self.top * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        return new_top, new_bottom
    def __str__(self):
        return str(self.top) + "\n--\n" + str(self.bottom)

half = Fraction(1, 2)
quarter = Fraction(1, 4)

print(half * quarter)
print(quarter)

# Quick Check 33.3
# Q1
Fraction.__mul__(half, quarter)
half.__mul__(quarter)
# Q2
print(Fraction.__str__(quarter))
print(quarter.__str__)
