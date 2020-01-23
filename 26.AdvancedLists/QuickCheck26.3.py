"""
This is Lesson 26. Advanced Operations with Lists
Get Programming: Learn to Code with Python

The split() function separates a string into a list based on the element you enter in the function's parameter
"""
#Q1
s1 = "abcdefghijklmnopqrstuvxyz"
s1_list = s1.split(" ")
print(s1_list)   # Doesn't do anything because s1 does not contain spaces

#Q2
s2 = "spaces and more spaces"
s2_list = s2.split(" ")
print(s2_list)

#Q3
print("The secret of life is 42".split("s"))