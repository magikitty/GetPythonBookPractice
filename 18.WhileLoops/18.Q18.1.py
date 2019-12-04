# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:45:36 2019

@author: elina

This is chapter 18. It is about repeating tasks while conditions hold true and
introduces while loops, break statements, continue statements
"""

# =============================================================================
# print("Q 18.1: This code has a bug, change one line to fix")
# num = 8
# guess = int(input("Guess my number: "))
# while guess != num:
#     guess = input("Guess again: ")  # Make INT!!!!
# print("Right!")
# =============================================================================

print("Q 18.1: Fixed code")
num = 8
guess = int(input("Guess my number: "))
while guess != num:
    guess = int(input("Guess again: "))
print("Right!")
