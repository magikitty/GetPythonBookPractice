# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:33:14 2019

@author: elina

This is Lesson 19: Capstone Project; Scrabble, the Art Edition
This is the solution from the book
"""
# All the valid art words
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

# Initialize variables
start = 0
end = 0
newline = "\n"
tupValidWords = ()
foundWords = ()
tiles = "ahriubetkndwng"

# Save art words into a tuple
for char in art_words:
    if char == newline:
        word = art_words[start:end]
        tupValidWords = tupValidWords + (word,)
        start = end + 1
        end += 1
    else:
        end += 1

# Check if word can be made with letters
for word in tupValidWords:
    tilesLeft = tiles
    for letter in word:
        if letter not in tilesLeft:
            break
        else:
            index = tilesLeft.find(letter)
            tilesLeft = tilesLeft[0:index] + tilesLeft[index + 1:]
        if len(word) == len(tiles) - len(tilesLeft):
            foundWords = foundWords + (word,)
print("Your possible words are:", foundWords)
