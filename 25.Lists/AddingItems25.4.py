"""
This is Lesson 25: Working with lists
Get Programming: Learn to Code With Python

There are three ways to add items to lists: append, insert, and extend
"""
# Append adds one item to the end of the list (last index position)
grocery_list = ["boinky beans", "milk"]
grocery_list.append("bananas")
print(grocery_list)

# Insert adds one item into the specified index position
cat_breeds = ["Persian", "Scottish fold", "Wild cat"]
cat_breeds.insert(2, "Super fluffy cat")
print(cat_breeds)

# Extend adds all items from one list to the end of another list
fun_things = ["My Beboo", "Nintendo Switch", "swimming", "songs"]
more_fun_things = ["TV shows", "warm houses", "parks"]
fun_things.extend(more_fun_things)
print(fun_things)
