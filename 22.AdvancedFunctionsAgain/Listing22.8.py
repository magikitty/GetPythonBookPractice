"""
This is Lesson 22: Advanced operations with functions
Get Programming: Learn to Code With Python

The following is practice for passing a function object as a paramter to another function
Based on Listing 22.8
"""

def pasta(kind_of_pasta):       # kind_of_pasta is a parameter for pasta()
    print("-*-*-*-*-*-*-*-")
    print(kind_of_pasta())      # The paranthesis for kind_of_pasta() indicate that it is a function call
    print("-*-*-*-*-*-*-*-")

def carbonara():
    carbonara_meal = "Tagliatelle\nCream\nBacon\nCheese"
    return carbonara_meal

def napoletana():
    napoletana_meal = "Spaghetti\nTomato\nGarlic"
    return napoletana_meal

pasta(carbonara)