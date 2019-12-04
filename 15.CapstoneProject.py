# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:27:24 2019

@author: elina
"""

# This is Capstone Course 15: Choose-your-own-adventure story!
# This capstone course is focused on conditionals and branching

print("Welcome to the Fun Forest Adventure Game!")

space = ("\n")
# =============================================================================
# print(space)
# =============================================================================

print(space, "You find yourself in the middle of a forest all by yourself. "
      "You're not sure how you got here, but you need to get back to "
      "civilization...", space)

# =============================================================================
# print(space)
# =============================================================================
# Explain how the game works
print("Available commands are in CAPITAL letters. Type in the first letter "
      "of the command in order to advance.")
print("Any other commands will end the game.")

print(space)

# First branch
print("You look around, and all you see is trees. But you decide to get "
      "moving because you won't get anywhere standing still.")

do = input("Do you head off RIGHT or LEFT? ")
do = do.lower()

if do == "r":
    print("You find a bubbling brook with clear water and realize that you "
          "are very thirsty.")

    do = input("Do you DRINK from the brook or MOVE on? ")
    do = do.lower()
    if do == "d":
            print("You plunge your face into the brook and take a nice "
                  "long drink. Just like a horsey drinking from a trough.")
    elif do == "m":
            print("Suspicious of anything that doesn't come in a plastic "
                  "bottle, you decide to move on and explore further into "
                  "the forest.")

elif do == "l":
    print("You see a clearing through the trees and walk towards it. On the "
          "side of the clearing you spot two different berry bushes and "
          "realize you are desperately hungry.")

    do = input("Do you eat the large PURPLE berries or the small RED berries?")
    do = do.lower()
    if do == "p":
        print("The purple berries are sweet and delicious and you immidiately "
              "start to feel energized.")
    elif do == "r":
        print("You shove a handful of red berries into your mouth and for a "
              "moment you feel wonderful. Then quite suddenly you keel over "
              "and fall face first into the forest floor.")
