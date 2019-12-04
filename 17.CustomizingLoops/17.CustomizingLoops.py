# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:44:09 2019

@author: elina

This is chapter 17: Customizing Loops
"""

print("Quick Check 17.1")
for i in range(0, 9):
    print("1. ", i)
for i in range(3, 8):
    print("2. ", i)
for i in range(-2, 3, 2):
    print("3. ", i)
for i in range(5, -5, -3):
    print("4. ", i)
for i in range(4, 1, 2):
    print("5. ", i)

# my first method
print("Quick Check 17.2")
word = input("Enter a word or sentence: ")
for char in word:
    if char == "a":
        print("vowel")
    elif char == "e":
        print("vowel")
    elif char == "i":
        print("vowel")
    elif char == "o":
        print("vowel")
    elif char == "u":
        print("vowel")
    else:
        print(char)

# my second method, based on answer in book
vowels = "aeiou"
word = input("Enter a word or sentence: ")
for char in word:
    if char in vowels:
        print("vowel")
    else:
        print(char)

# This is quicker than interating over each index
print("Listing 17.1: A for loop that iterates over each character in a string")
for char in "Python is fun so far!":
    print("The character is", char)

print("Listing 17.2: A for loop that iterates over each index in a string")
my_string = "Python is fun so far!"
len_string = len(my_string)
for i in range(len_string):
    print("the character is", my_string[i])

print("Q 17.1")
counter = 0
for num in range(2, 101, 2):  # finds the even numbers
    if num % 6 == 0:  # finds the even numbers divisble by 6
        counter += 1
# only prints last counter value when print statement is not nested under if
print(counter, "numbers are even and divisible by 6.")

print("Q 17.2 A: Counter is number of books left")
num = int(input("Enter a number: "))
counter = num
for i in range(num):
    if counter > 1:
        print(counter, "Python books on the shelf", counter, "Python books. "
              "Take one down, pass it around", counter - 1, "books left.")
    elif counter <= 1:
        print(counter, "Python book on the shelf", counter, "book on Python. "
              "Take one down, pass it around, no more books!")
    counter -= 1

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
for iteration in range(num):

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
