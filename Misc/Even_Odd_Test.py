# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:50:52 2019

@author: elina
"""

print("Is it even or odd? Let's find out!")

# User inp
number_input = int(input("Enter a number: "))

# Modulo operation
# conversion = number_input % 2
if number_input % 2 == 0:
    print(number_input, "is even!")
else:
    print(number_input, "is odd!")
