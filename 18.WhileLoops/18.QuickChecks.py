# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:17:29 2019

@author: elina

This is chapter 18. It is about repeating tasks while conditions hold true and
introduces while loops, break statements, continue statements
"""

print("Quick Check 18.1")
# Initialize variables
num = 11  # my secret number
num_user = int(input("Guess what number I'm thinking of between 1 and 14: "))
tries = 1

# While loop
while num_user != num:
    print("Nope! You have guessed", tries, "times.")
    num_user = int(input("Guess again: "))
    tries += 1

print("You got it! My number was", num)

print("\n")

print("Quick Check 18.2: The While Loop")
# The While Loop
password = "robot flower fort graph"
space_count = 0
i = 0

while i < len(password):
    if password[i] == " ":
        space_count += 1
    i += 1
print("There are", space_count, "spaces")

print("\n")

print("Quick Check 18.2: The For Loop")
# The above while loop rewritten as a for loop
password = "robot flower fort graph"
space_count = 0

for char in password:
    if char == " ":
        space_count += 1
print("There are", space_count, "spaces")

print("\n")

print("Quick Check 18.3: My answer")
word = "beboo"
guess = input("Guess my secret word (you have 21 tries): ")
tries_max = 21
tries = 1

while guess != word:
    if tries < 21:
        print("Nope! You have guessed", tries, "times")
        guess = input("Guess again: ")
    if tries == 21:
        print("You have guessed", tries, "times. You have no more tries left.")
        break

    tries += 1

if tries <= 21 and guess == word:
        print("You got it! The secret word was", word, "Yaaaaay!")

print("\n")

print("Quick Check 18.3: Book answer")
word = "snake"
guess = input("What's my secret word? ")
tries = 1

while guess != word:
    guess = input("What's my secret word? ")
    if tries == 20 and guess != word:
        print("You did not get it.")
        break
    tries += 1
