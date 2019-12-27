"""
This is Lesson 25: Working with lists
Get Programming: Learn to Code With Python
"""

L = ["one", "three", "two", "three", "four", "three", "three", "five"]

print(L.count("one"))
print(L.count("three"))
print(L.count("zero"))
print(len(L))
print(L.index("two"))
print(L.index("three"))
# print(L.index("zero"))   # error because "zero" is not included in the list
