# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:08:45 2019

@author: elina

This is Lesson 19: Capstone Project; Scrabble, the Art Edition
This is my solution
"""
import random

# Art word (in a string separated by new lines)
art_words = """art
pen
ink
hue
clay
draw
paint
brush
shade
shape
music
crayon
canvas
pencil
colour
sketch
stencil
drawing
shading
charcoal
watercolour
"""

# Define variables
newline = "\n"
word = ""
tup_art_words = ()
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_len = len(alphabet)


# Separate words in string
# Save the word into the tuple
for char in art_words:
    if char == newline:
        tup_art_words = tup_art_words + (word,)
        word = ""
    else:
        word = word + char

# Pick 30 random letters (letter tiles) from alphabet and print letter tiles
counter = 0
letter_tiles = ""

while counter < 30:
    letter_index = random.randrange(0, alphabet_len)  # picks random num
    letter = alphabet[letter_index]  # returns value at random num index pos
    letter_tiles = letter_tiles + letter
    counter = counter + 1
if counter == 30:
    print("Your letter tiles are:", letter_tiles)

# Print words that can be made with letter tiles
counter_word = 0
word_temp = ""
word_possible = ""

for word in tup_art_words:
    for char in word:
        if char in letter_tiles:
            word_temp = word_temp + char
        if word_temp == word:
            word_possible = word_possible + word + " "
    word_temp = ""
    counter_word += 1

print("Your possible words are:", word_possible)
