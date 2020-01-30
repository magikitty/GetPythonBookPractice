"""
This is Lesson 26. Advanced Operations with Lists
Get Programming: Learn to Code with Python
"""
# Function to test if two lists are permutations of each other


# def is_permutation(L1, L2):
#     L1.sort()
#     L2.sort()
#     if L1 == L2:
#         return True
#     elif L1 != L2:
#         return False


def is_permutation(L1, L2):
    L1.sort()
    L2.sort()
    return L1 == L2    # will return True or False


print(is_permutation([1, 2, 3], [3, 2, 1]))
print(is_permutation([1, 2, 4], [3, 2, 1, 5, 8]))
print(is_permutation([4, 2, 3, 9], [4, 3, 9, 2]))
