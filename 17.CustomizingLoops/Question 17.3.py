# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:31:06 2019

@author: elina
"""

print("Q 17.3: My answer")
# Initialise variables
names = input("Enter two or more names: ")
name = ""
hi = "Oh hi "
space = " "
counter = 0
length = len(names)

# Loop through input and display output
for char in names:
    if char != space:
        name = name + char
    elif char == space:
        print(hi + name)
        name = ""
    if counter == length - 1:
        print(hi + name)

    counter += 1  # used to find the last char in the names string

print("Q 17.3: Book answer")
names = input("Tell me some names, separated by spaces: ")
name = ""

for ch in names:
    if ch == " ":
        print("Hi", name)
        name = ""
    else:
        name += ch

# deal with the last name given (does not have space after it)
lastspace = names.rfind(" ")
print("Hi", names[lastspace + 1:])
