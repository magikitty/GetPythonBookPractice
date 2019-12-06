# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:44:56 2019

@author: elina
"""

""" Lesson 11 is about printing values, asking for user input and storing input
to do operations with it.
Note: functions were not part of the lesson, but made testing easier."""

# creates a (double) line space
space = "\n"


def printVariables():
    print("Quick Check 11.1")
    # What is printed?
    print(13-1)
    "nice"
    a = "nice"
    b = " is the new cool"
    print(a.capitalize() + b)


def capitalizeChoice():
    print("Quick Check 11.2")
    sweet = "cookies"
    savory = "pickles"
    num = 100
    print(num, savory, "and", num, (sweet + "."))
    print("I choose the " + sweet.upper() + "!")


def getUserInput():
    print("Quick Check 11.3")
    input("What's your secret? ")
    input("What's your favourite colour? ")
    input("Please enter one of the following symbols: #, $, %, &, or * : ")


def faveSong():
    print("Quick Check 11.4")
    fave_song = input("What's your favourite song? ")
    print(fave_song)
    print(fave_song)
    print(fave_song)


def celebrityName():
    name_celeb = input("What's the first and last name of a celebrity? ")
    space = name_celeb.find(" ")
    name_first = name_celeb[0:space]
    name_last = name_celeb[space+1:len(name_celeb)]
    print(name_first)
    print(name_last)


def intSquare():
    print("Listing 11.5")
    # Typecasting user input from string to int
    user_input = input("Enter a number to find square of: ")
    num = int(user_input)
    print(num * num)


def floatSquare():
    print("Quick Check 11.5")
    # Typecasting user input from string to float
    user_input = input("Enter a number to find square of: ")
    num = float(user_input)
    print(num * num)


def multiplyNumbers():
    print("Listing 11.6")
    # Calculations with more than one user input
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a second number: "))
    print(num1, "*", num2, "=", num1 * num2)


def powerOf():
    print("Q.11.1")
    # ask user for two nums (b&e) and show b to power of e
    b = int(input("Enter a number: "))
    e = int(input("Enter another number: "))
    print(b, "**", e, "=", b**e)


def inputAgeName():
    print("Q11.2")
    # Get name and age, say hi, show age in 25 years
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_age_25 = str(user_age + 25)
    print("Hi", user_name + "!", "In 25 years you will be", user_age_25 + "!")


powerOf()
inputAgeName()
