# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:31:24 2019

@author: elina
"""

# Get user input
minutes_to_convert = int(input("Enter number of minutes: "))

# Set up conversions from minutes to hours and minutes (variables)
number_decimal_hours = minutes_to_convert / 60
number_hours = int(number_decimal_hours)
number_minutes = minutes_to_convert % 60

# Print output
print("Hours")
print(number_hours)
print("Minutes")
print(number_minutes)
