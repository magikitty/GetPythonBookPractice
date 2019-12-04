# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:25:09 2019

@author: elina

This is chapter 17: Customizing Loops, These are Q17.1 - 17.3
"""

print("Q 17.1")
counter = 0
for num in range(2, 101, 2):  # finds the even numbers
    if num % 6 == 0:  # finds the even numbers divisble by 6
        counter += 1
        print(counter)

print("Q 17.2 A: Counter is number of books left")
num = int(input("Enter a number: "))
counter = num + 1
for i in range(num):
    counter -= 1  # good, but counter is used too early
    if counter > 1:
        print(counter, "Python books on the shelf", counter, "Python books. "
              "Take one down, pass it around", counter - 1, "books left.")
    elif counter <= 1:
        print(counter, "Python book on the shelf", counter, "book on Python. "
              "Take one down, pass it around, no more books!")

print("\n")

print("Q 17.2 B: minus the counter from books left, confusing method")
num = int(input("Enter a number: "))
num = num + 1
counter = 0
for i in range(num):
    counter += 1
    if counter != num - 1 and counter != num:
        print(num - counter, "Python books on the shelf", num - counter,
              "Python books. "
              "Take one down, pass it around", (num - counter) - 1,
              "books left.")
    elif counter == num - 1:
        print(num - counter, "Python book on the shelf", num - counter,
              "book on Python. "
              "Take one down, pass it around, no more books!")

print("\n")

print("Q 17.2 C: Jono's implementation, put counter at end")
# 1. Initialise variables
num = int(input("Enter a number: "))
counter = num

# 2. Iterate through num range
for i in range(num):

    if counter > 1:
        print(counter, "Python books on the shelf", counter, "Python books. "
              "Take one down, pass it around,", counter - 1, "books left.")

    else:
        print(counter, "Python book on the shelf", counter, "book on Python. "
              "Take one down, pass it around, no more books!")
    counter -= 1

print("\n")

print("Q 17.2 D: Answer from the book; no counter needed; short")
count = int(input("Enter a number: "))
for n in range(count, 0, -1):
    if count == 1:
        print(n, "Python book on the shelf", n, "book on Python. "
              "Take one down, pass it around, no more books!")
    else:
        print(n, "Python books on the shelf", n, "Python books. "
              "Take one down, pass it around", n - 1, "books left.")

print("\n")

print("Q 17.3: My answer")
# Initialise variables
names = input("Enter two or more names: ")
name = ""
hi = "Oh hi "
space = " "
counter = 0
length = len(names)

# Loop through input and display output
for char in names:
    if char != space:
        name = name + char
    elif char == space:
        print(hi + name)
        name = ""
    if counter == length - 1:
        print(hi + name)

    counter += 1  # used to find the last char in the names string

print("Q 17.3: Book answer")
names = input("Tell me some names, separated by spaces: ")
name = ""

for ch in names:
    if ch == " ":
        print("Hi", name)
        name = ""
    else:
        name += ch

# deal with the last name given (does not have space after it)
lastspace = names.rfind(" ")
print("Hi", names[lastspace + 1:])
