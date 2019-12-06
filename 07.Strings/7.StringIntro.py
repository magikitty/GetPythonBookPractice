# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:52:14 2019

@author: elina

These are Chapter 7 Qs
"""
new_line = "\n"

# Quick Check 7.3
print("Quick Check 7.3")

print("hey there"[1])
print("TV guide"[2])
code = "L33t hax0r5"
print(code[0])
print(code[-4])
print("bananaboo"[3])
print("bananaboo"[-3])

# Quick Check 7.4
print("Quick Check 7.4")

print("it's not impossible"[1:2:1])
print("Keeping up with Python"[-1:-20:-2])
secret = "mai p455w_zero_rD"
print(secret[-1:-8])

"""
# Extra practice
print("it's not impossible"[1:2:1])   # t
print("Keeping up with Python"[-1:-20:-2])   # nhy hi p gie
secret = "mai p455w_zero_rD"
s_len = len(secret)
step = s_len-1
print(len(secret))
print(secret[-1:-50:-step])   # Dr_orez
"""

# Quick Check 7.5
print("Quick Check 7.5")
a = "python 4 ever&EVER"
print(a.capitalize())
print(a.swapcase())
print(a.upper())
print(a.lower())

print(new_line)

# Getting the length of the string
print("Len practice")
word = "banana"
# print(len(word))
# print(word.len())
print(word.lower())

print(new_line)

# Question 7.1
print("Q 7.1")
greeting = "Guten Morgen"
# in long form with slicing
greeting_cut = greeting[2:5]
greeting_cut_caps = greeting_cut.upper()
print(greeting_cut_caps)
# in short form with slicing (positive)
print(greeting[2:5].upper())
# in short form with slicing (negative)
print(greeting[-10:-7].upper())
# with indexes
print(greeting[2].upper() + greeting[3].upper() + greeting[4].upper())
# print(greeting[2].upper(), greeting[3].upper(), greeting[4].upper())

print(new_line)

# Question 7.2
print("Question 7.2")
word = "RaceTrack"
# slicing with positive
print(word[1:4].capitalize())
# slicing with negative
print(word[-8:-5].capitalize())
# with indeces
print(word[-8].upper() + word[-7] + word[-6])
print(word[1].upper() + word[2] + word[3])
