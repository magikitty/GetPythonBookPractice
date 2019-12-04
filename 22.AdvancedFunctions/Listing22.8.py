# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:59:52 2019

@author: elina
"""


def sandwich(kind_of_sandwich):
    print("-------------")
    print(kind_of_sandwich())
    print("-------------")


def blt():
    my_blt = "bacon\nlettuce\ntomato"
    return(my_blt)


def breakfast():
    my_ec = "egg\ncheese"
    return my_ec


def custom(ingredient1, ingredient2):
    my_cust = ingredient1 + ingredient2
    return my_cust


print(sandwich(blt))
