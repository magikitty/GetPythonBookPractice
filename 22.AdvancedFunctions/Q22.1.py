# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:06:51 2019

@author: elina

Lesson 22: Advanced Operations with Functions
"""


def area(shape, n):
    return shape(n)


def circle(radius):
    return 3.14*radius**2


def square(length):
    return length*length


print(area(square, 5))

print(area(circle, 10))
