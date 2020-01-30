"""
This is Lesson 25: Working with lists
Get Programming: Learn to Code With Python
"""

# Q1
one = [1]
one.append("1")
print(one)

# Q2
zero = []
zero.append(0)
zero.append(["zero"])
print(zero)

# Q3
two = []
three = []
three.extend(two)
print(three)

# Q4
four = [1, 2, 3, 4]
four.insert(len(four), 5)
print(four)
four.insert(0, 0)
print(four)
