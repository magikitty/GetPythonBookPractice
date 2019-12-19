"""
This is Lesson 22: Advanced operations with functions
Get Programming: Learn to Code With Python
"""
# Q 22.1

def area(shape, n):
    return shape(n)

def circle(radius):
    return 3.14*radius**2

def square(length):
    return length*length

print(circle(10))
print(square(5))
print(circle(4/2))