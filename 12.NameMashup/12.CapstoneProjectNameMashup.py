# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:27:59 2019

@author: elina
"""

"""This Capstone Project is about getting user input for two names
(each consisting of a forename and surname) and mashing the two names
together
Note: This is my solution (without looking at the book answer)"""

print("Welcome to the Name Mashup Game!")

# Get and store user input for names
s1 = input("Enter a first and last name: ")
s2 = input("Enter a second first and last name: ")

# Split and store as variables full names into first and last names
space = s1.find(" ")
s1Fore = s1[0:space]
s1Sur = s1[space+1:len(s1)]

space2 = s2.find(" ")
s2Fore = s2[0:space2]
s2Sur = s2[space2+1:len(s2)]

# Split up names (in half)

# S1 Forename in halves
s1ForeHalf1 = s1Fore[0:int(len(s1Fore)/2)]
s1ForeHalf2 = s1Fore[int(len(s1Fore)/2):len(s1Fore)]

# s2 Forename in halves
s2ForeHalf1 = s2Fore[0:int(len(s2Fore)/2)]
s2ForeHalf2 = s2Fore[int(len(s2Fore)/2):len(s2Fore)]

# s1 Surname in halves
s1SurHalf1 = s1Sur[0:int(len(s1Sur)/2)]
s1SurHalf2 = s1Sur[int(len(s1Sur)/2):len(s1Sur)]

# s2 Surname in halves
s2SurHalf1 = s2Sur[0:int(len(s2Sur)/2)]
s2SurHalf2 = s2Sur[int(len(s2Sur)/2):len(s2Sur)]

# Combine parts of names
ForeNew1 = s1ForeHalf1.capitalize() + s2ForeHalf2.lower()
SurNew1 = s1SurHalf1.capitalize() + s2SurHalf2.lower()

ForeNew2 = s2ForeHalf1.capitalize() + s1ForeHalf2.lower()
SurNew2 = s2SurHalf1.capitalize() + s1SurHalf2.lower()

print("Great! Here are two new names for you to pick from: ")
print(ForeNew1, SurNew1)
print(ForeNew2, SurNew2)

# Test
# =============================================================================
# print(s1Fore)
# print(s1Sur)
# print(s2Fore)
# print(s2Sur)

# print("s1.1 fore", s1ForeHalf1)
# print("s1.2 fore", s1ForeHalf2)
# print("s2.1 fore", s2ForeHalf1)
# print("s2.2 fore", s2ForeHalf2)
# print("s1.1 sur", s1SurHalf1)
# print("s1.2 sur", s1SurHalf2)
# print("s2.1 sur", s2SurHalf1)
# print("s2.2 sur", s2SurHalf2)
# =============================================================================
