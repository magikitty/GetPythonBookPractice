# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:54:40 2019

@author: elina
"""

print("Q1. Calculating tip")


def calculate_total(price, percent):
    total = float(price + percent * price)
    return total


print("Q2. Call previous function")


def new_total():
    calculate_total(20, 0.15)
    print(calculate_total)
