"""
This is Lesson 32. Working with your own object types
Get Programming: Learn to Code with Python
"""

list_fruits = ["orange", "mango", "pear", "pineapple", "apple"]


class Stack(object):
    def __init__(self):
        self.stack = []

    def add_list(self, list_to_add):
        for i in range(0, len(list_to_add)):
            item = list_to_add[i]
            self.stack.append(item)
        return self.stack


fruit_stack = Stack()
print(fruit_stack.add_list(list_fruits))
