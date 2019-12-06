# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:45:12 2019

@author: elina
"""
# This lesson was about understanding what simple error messages mean

print("Question 9.1")

one = "hello"[-6]
print(one)  # IndexError: string index out of range

two = "hello".upper("h")
print(two)  # TypeError: upper() takes no arguments (1 given)

three = "hello".replace("a")  # TypeError: replace() takes at least 2 arguments (1 given)

four = "hello".count(3)  # TypeError: must be str, not int

five = "hello".count(h)  # NameError: name 'h' is not defined

six = "hello" * "2"  # TypeError: can't multiply sequence by non-int of type 'str'
