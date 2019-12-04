# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:27:54 2019

@author: elina

This is chapter 18. It is about repeating tasks while conditions hold true and
introduces while loops, break statements, continue statements
"""

print("Q 18.2")
play = input("Do you want to play a game? (yes/y/no/n) ")
play = play.lower()
num = 3

while play == "yes" or play == "y":
    guess = int(input("Ok! Guess what number I'm thinking of between 1-10: "))
    while guess != num:
        guess = int(input("Nope, guess again: "))
    if guess == num:
        print("You got it! The number I was thinking of was", num)
    play = input("Do you want to play again? (yes/y/no/n) ")
    play = play.lower()
if play == "no" or play == "n":
    print("Ok, byeeee!")
