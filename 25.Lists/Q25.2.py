"""
This is Lesson 25: Working with lists
Get Programming: Learn to Code With Python
"""
# L = "some", "stuff", "wow"


def unique(L):
    unique_L = []
    for n in L:
        if n not in unique_L:
            unique_L.append(n)
    return unique_L


print(unique(["some", "stuff", "wow", "wow", "woop", "woop", "woop"]))
