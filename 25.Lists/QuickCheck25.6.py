"""
This is Lesson 25: Working with lists
Get Programming: Learn to Code With Python

You can modify an element in a list by accessing its index value and assigning it a new value
"""

L = [1, 2, 3, 5, 7, 11, 13, 17]

L[3] = 4
print(L)
L[4] = 6
print(L)
L[-1] = L[0]
print(L)
L[0] = L[1] + 1
print(L)
