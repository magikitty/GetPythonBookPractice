# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:21:55 2019

@author: elina
"""

# Lesson 10 is about Tuple objects (sequences of any kind of object)

print("Quick Check 10.1")
print("carnival",)
print("ferris wheel", "rollercoaster")
print("tickets")  # not a tuple
print((), ())

print("Quick Check 10.2")
print(len(("hi", "hello", "hey", "hi")))
print(len(("abc", (1, 2, 3))))
print(len(((1, 2),)))
print(len(()))

print("Quick Check 10.3")
print(("abc", (1, 2, 3))[1])
print(("abc", (1, 2, "3"))[1][2])
print(("abc", (1, 2), "3", 4, ("5", "6"))[1:3])
a = 0
t = (True, "True")
print(t[a])

print("Quick Check 10.4")
print(len("abc") * ("no",))
print(2 * ("no", "no", "no"))
print((0, 0, 0) + (1,))
print((1, 1) + (1, 1))

print("Quick Check 10.5")
s = "strong"
w = "weak"
new = (s, w) = (w, s)
print(new)
yes = "affirmative"
no = "negative"
yorp = (yes, no) = (no, yes)
print(yorp)

# slicing practice
s1 = "catface"
s2 = s1[0:2]
# print(s2)

print("Q 10.1: My Way")
t = ()
count = 3
word = "echo"
word_two = word[1:]
word_three = word[2:]
word_four = word[3:]
t = t + ((word,) * count) + ((word_two,) * count) + \
      ((word_three,) * count) + ((word_four,) * 3)
print(t)

print("Q 10.1: Answer from book")
word = "echo"
t = ()
count = 3

echo = (word,)
echo *= count  # same as echo = echo * count
cho = (word[1:],)
cho *= count
ho = (word[2:],)
ho *= count
o = (word[3:],)
o *= count

t = echo + cho + ho + o
print(t)
