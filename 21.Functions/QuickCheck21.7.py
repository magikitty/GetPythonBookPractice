# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:19:49 2019

@author: elina
"""

who = "Hector"
what = "eating"
thing = "bananas"
number = 8


def make_sentence(who, what):
    doing = who + " is " + what
    return doing


def add(who, what):
    doing = who + what
    return doing


def show_story(person, action, number, thing):
    what = make_sentence(person, action)
    num_times = str(number) + " " + thing
    my_story = what + " " + num_times
    print(my_story)


your_story = show_story(who, what, number, thing)
