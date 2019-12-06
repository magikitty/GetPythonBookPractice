# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:27:49 2019

@author: elina

This is Lesson 16: repeating tasks with loops
"""

print("Quick Check 16.1")
for wow in range(8):
    print("cray")
for i in range(10):
    print("fish")
for i in range(10):
    print(i)

print("Quick Check 16.2")
print(range(1))
print(range(5))
print(range(100))

for i in range(1):
    print(i)
for i in range(5):
    print(i)
for i in range(100):
    print(i)

print("practice listing 16.2")
num = 12
for i in range(num):
    print(i)

print("Q 16.1")
# using a for loop
num = int(input("Enter an integer: "))
for i in range(num):
    print("Hello")

# without using a for loop
num2 = int(input("Enter an integer2: "))
word = "Hello"
space = " "
print(num2 * (word + space))
