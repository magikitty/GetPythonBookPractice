"""
This is Lesson 21: Achieving modularity and abstaction with functions in
Get Programming: Learn to Code With Python
"""

# Quick Check 21.6

def guessed_card(number, suit, bet):
    money_won = 0
    guessed = False
    if number == 7 and suit == "hearts":
        money_won = 10*bet
        guessed = True
    else:
        money_won = bet/10
    return("You won " + str(money_won), "Your guess was " + str(guessed))    # returns amount of money_won and if guess was True or False

print(guessed_card(7, "hearts", 15))

print(guessed_card("7", "hearts", 15))

print(guessed_card(9, "spades", 100))

(guessed_card(9, "spades", 100))   # doesn't print anything because the function does not print anything

(first_return, second_return) = guessed_card("eight", "hearts", 80)
print(first_return)
print(second_return)
