# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:32:42 2019

@author: elina
"""


def person(age):
    print("I am a person")

    def student(major):
        print("I like learning")

        def vacation(place):
            print("But I need breaks")
            print(age, "|", major, "|", place)
        return vacation
    return student


person(12)("Math")("beach")
person(23)("Law")("Florida")
