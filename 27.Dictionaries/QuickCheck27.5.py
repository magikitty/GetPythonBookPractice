"""
This is Lesson 27. Dictionaries as Maps Between Objects
Get Programming: Learn to Code with Python

Introduction to dictionaries
"""

employees = {"John": 34, "Mary": 24, "Erin": 50}
for em in employees:
    employees[em] += 1
for em in employees.keys():
    print(employees[em])
