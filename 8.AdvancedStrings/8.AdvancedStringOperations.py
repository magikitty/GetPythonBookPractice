# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:52:58 2019

@author: elina
"""
new_line = "\n"

# Lesson 8

print("Quick Check 8.1")

a = "python 4 ever&EVER"
print(a.find("E"))
print(a.find("eve"))
print(a.rfind("rev"))
print(a.rfind("VER"))
print(a.find(" "))
print(a.rfind(" "))

print(new_line)

print("Quick Check 8.2")

a = "python 4 ever&EVER"
print("on" in a)
print("" in a)
print("2 * 2" in a)

print(new_line)

print("Quick Check 8.3")

a = "python 4 ever&EVER"
print(a.count("ev"))
print(a.count(" "))
print(a.count(" 4 "))
print(a.count("eVer"))

print(new_line)

print("Quick Check 8.4")

a = "Raining in the spring time."
print(a.replace("R", "r"))
print(a.replace("ing", ""))
print(a.replace("!", "."))
b = a.replace("time", "tiempo")
print(b)

print(new_line)

print("Quick Check 8.5")
# Q1
q_one = "la" + "la" + "Land"
print(q_one)

# Q2
q_two = "USA" + " vs " + "Canada"
print(q_two)

# Q2
b = "NYc"
c = 5
q_three = b * c
print(q_three)

# Q3
colour = "red"
shape = "circle"
number = 3
q_four = number * (colour + "-" + shape)
print(q_four)

print(new_line)

print("Q 8.1")
# Method 1
sentence_start = "Eat Work Play Sleep repeat"
sentence = sentence_start.lower()
word_work = sentence[4:8]
word_play = sentence[9:13]
sentence_new = (word_work + "ing") + " " + (word_play + "ing")
print(sentence_new)

# Method 2
sentence_start = "Eat Work Play Sleep repeat"
sentence_a = sentence_start.replace(" ", "ing ")
sentence_b = sentence_a[7:22]
sentence_final = sentence_b.lower()
print(sentence_final)

# Method 3
sentence_start = "Eat Work Play Sleep repeat"
sentence_1 = sentence_start.replace("Work", "working")
sentence_2 = sentence_1.replace("Play", "playing")
sentence_3 = sentence_2.replace("Eat ", "")
sentence_4 = sentence_3.replace(" Sleep repeat", "")
print(sentence_4)
