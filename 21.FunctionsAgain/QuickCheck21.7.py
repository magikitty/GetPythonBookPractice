"""
This is Lesson 21: Achieving modularity and abstaction with functions in
Get Programming: Learn to Code With Python
"""

# Quick Check 21.7

def make_sentence(who, what):
    doing = who + " is " + what
    return doing

def show_story(person, action, number, thing):
    what = make_sentence(person, action)
    num_times = str(number) + " " + thing
    my_story = what + " " + num_times
    print(my_story)

who = "Uncle Bob"
what = "flying"
thing = "spaceships"
number = 5

sentence = make_sentence(who, thing)  # doesn't print anything
print(make_sentence(who, what))
your_story = show_story(who, what, number, thing)
my_story = show_story(sentence, what, number, thing)
print(your_story)  # prints None because the function show_story does not return anything