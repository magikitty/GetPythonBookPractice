# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:52:27 2019

@author: elina
"""

""" Lesson 14 is about making more-complicated decisions in code """

print("Quick Check 14.3")
num_a = int(input("Enter number a: "))
num_b = int(input("Enter number b: "))

if num_a < 0 and num_b < 0:
    print("Both negative")

print("Quick Check 14.4")
num = int(input("Enter an integer: "))
if num > 0:
    print("num is positive")
elif num < 0:
    print("num is negative")
else:
    print("num is zero")

print("Q 14.1")
print("Hello! This program will tell you the relation between two numbers.")
num_a = int(input("Enter a number: "))
num_b = int(input("Enter a second number: "))

if num_a == num_b:
    print("The numbers are equal")

elif num_a < num_b:
    print("The first number is smaller than the second number")

elif num_a > num_b:
    print("The first number is greater than the second number")

print("Q 14.2")
print("This program will tell you if your input contains all the vowels or \
      starts with a and ends with z.")

user_input = input("Say something: ")

# =============================================================================
# The below doesn't work:
# if "a" and "e" and "i" and "o" and "u" in user_input:
#     print("You have all the vowels!")
# =============================================================================

if "a" in user_input and "e" in user_input and "i" in user_input and "o" in \
   user_input and "u" in user_input:
    print("You have all the vowels!")

else:
    print("You don't have all the vowels!")

if user_input[0] == "a" and user_input[-1] == "z":
    print("And it's sort of alphabetical!")
