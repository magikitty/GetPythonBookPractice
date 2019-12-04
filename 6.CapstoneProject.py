# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 18:58:48 2019

@author: elina
"""
print("Method 1:")

# Set up the input
minutes_to_convert = 123

# Conversions: minutes to hours and minutes
number_decimal_hours = minutes_to_convert / 60
number_hours = int(number_decimal_hours)
number_decimal_minutes = number_decimal_hours - number_hours
number_minutes = round(number_decimal_minutes * 60)

# Set up the output
print("Hours")
print(number_hours)
print("Minutes")
print(number_minutes)

# Test
"""
print("Test")
print(number_decimal_hours)
print(number_hours)
print(number_decimal_minutes)
print(number_minutes)
"""
print("Method 2:")

# Set up the input
minutes_to_convert = 123

# Conversions: minutes to hours and minutes
number_decimal_hours = minutes_to_convert / 60
number_hours = int(number_decimal_hours)
# Modulo gives a whole number for mintues because int % int gives an int
number_minutes = minutes_to_convert % 60

# Set up the output
print("Hours")
print(number_hours)
print("Minutes")
print(number_minutes)
