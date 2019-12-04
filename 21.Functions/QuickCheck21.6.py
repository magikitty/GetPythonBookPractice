# -*- coding: utf-8 -*-
"""
Created on Sat May 25 09:49:50 2019

@author: elina
"""

print("Quick Check 21.6")


def guessed_card(number, suit, bet):
    money_won = 0
    guessed = False
    if number == 8 and suit == "hearts":
        money_won = 10 * bet
        guessed = True
    else:
        money_won = bet / 10
    return(money_won, guessed)


print(guessed_card(8, "hearts", 10))

(amount, did_win) = guessed_card("eight", "hearts", 80)
print(did_win)
print(amount)


def TimesTwo(number):
    return number * 2

# =============================================================================
# def GreetUser(name):
#     """Prints a greeting to the user"""
#     print("Hello " + name)
# 
# 
# def CountLetters(word):
#     print(len(word))
# 
# 
# GreetUser("Dave")
# 
# =============================================================================


ans = TimesTwo(3)
print(ans)
