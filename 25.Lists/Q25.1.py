"""
This is Lesson 25: Working with lists
Get Programming: Learn to Code With Python
"""

menu = []

# Q1
food = ["pizza", "beer", "fries", "wings", "salad"]
menu.extend(food)
print(menu)

# Q2
menu.insert(0, "salad")
menu.pop(1)
menu.pop(1)
menu[3] = "pizza"
print(menu)

# Q3
menu[1] = "quinoa"
menu[2] = "steak"
menu.pop(3)
print(menu)
