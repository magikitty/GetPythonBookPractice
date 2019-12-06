# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 22:24:49 2019

@author: elina
"""

# Lesson 6 Practice

# Q 6.1
print("Q 6.1")
temperature_farenheit = float(input("Enter temperature Farenheit: "))
temperature_celsius = (temperature_farenheit - 32) / 1.8
print("The temperature in Celsius is: ", temperature_celsius)

# Q 6.2

print("Q 6.2")
# Enter number of miles
# number_miles = 5
number_miles = float(input("Enter number of miles: "))

# Convert miles to km
number_km = number_miles / 0.62137

# Convert km to m
# number_meters = number_km * 1000

# last argument in round specifies number of decimal places
number_meters = round(number_km * 1000, 2)

# Print result
print("Miles:")
print(number_miles)
print("km:")
print(number_km)
print("meters:")
print(number_meters)
