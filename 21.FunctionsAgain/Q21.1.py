"""
This is Lesson 21: Achieving modularity and abstaction with functions in
Get Programming: Learn to Code With Python
"""

# Q1
def calculate_total(price, percent):
    total = float(price) + int(percent) * float(price)
    return total

print(calculate_total(10, 5))
