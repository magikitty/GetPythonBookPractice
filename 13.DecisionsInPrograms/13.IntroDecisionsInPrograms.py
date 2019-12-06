# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:19:49 2019

@author: elina
"""

""" Lesson 13 is about introducing decisions in programs, conditionals and
Boolean expressions """

print("Quick Check 13.3")
num = int(input("Enter number: "))
if num < 10:
    print("num is less than 10")
print("Finished")

print("Quick Check 13.4 Q1")
word = input("Enter a word (do not include spaces): ")
space_index = word.find(" ")
if space_index >= 0:
    print("You didn't follow the instructions! There is a space!")
print("Your word is:", word)

print("Quick Check 13.4 Q1 Book Answer")
word = input("Enter a word (do not include spaces): ")
if " " in word:
    print("You didn't follow the instructions! There is a space!")
print("Your word is:", word)

print("Quick Check 13.4 Q2")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum_num = num1 + num2
print("The sum of the numbers is:", sum_num)
if sum_num < 0:
    print("Wow, negative sum!")

print("Quick Check 13.6: Nested Code")
num_a = int(input("Enter number a: "))
num_b = int(input("Enter number b: "))
if num_a < 0:
    print("num_a", num_a, "is negative")
    if num_b < 0:
        print("num_b", num_b, "is negative")
print("Finished")

print("Quick Check 13.6: Unnested Code")
num_a = int(input("Enter number a: "))
num_b = int(input("Enter number b: "))
if num_a < 0:
    print("num_a", num_a, "is negative")
if num_b < 0:
        print("num_b", num_b, "is negative")
print("Finished")

print("Quick Check 13.7: My answer")
print("You are at the store and want to decide how much chocolate to get...")
price = float(input("How much does a bar of chocolate cost? "))
hungry = input("Are you hungry? (yes or no) ")
bars = 0

if hungry == "no":
    print("No chocolate for you! Stick to the list.")

if hungry == "yes":
    if price < 1:
        print("Buy AAAALLLL 100 chocolate bars!")
        bars = 100
    if 1 <= price <= 5:
        print("Buy 10 chocolate bars!")
        bars = 10
    if price > 5:
        print("Buy one chocolate bar.")
        bars = 1

if bars > 10:
    print("Cashier says: Oooooh someone's hungry!")

print("Q 13.2")
var = 0
if type(var) == int:
    print("I'm a numbers person")
if type(var) == str:
    print("I'm a words person")

print("Q 13.3")
input_user = input("Enter a word or sentence: ")
if " " in input_user:
    print("This string has spaces")

print("Q 13.4")
num_secret = 9
guess = int(input("Guess my number! "))
if guess < num_secret:
    print("Too low!")
if guess > num_secret:
    print("Too high!")
if guess == num_secret:
    print("You got it!")

print("Q 13.5")
input_user = int(input("Enter an integer: "))
absolute = abs(input_user)
print("The absolute value is", absolute)
