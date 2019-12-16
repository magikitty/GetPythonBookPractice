"""
This is Lesson 21: Achieving modularity and abstaction with functions in
Get Programming: Learn to Code With Python
"""

# Q1
def calculate_total(price, percent):
    total = float(price) + int(percent) / float(price)
    return total

print(calculate_total(100, 25))

# Q2
print(calculate_total(20, 15))

# Q3
my_price = 78.55
my_tip = 20
new_total = calculate_total(my_price, my_tip)
print("Your new total is " + str(new_total))
