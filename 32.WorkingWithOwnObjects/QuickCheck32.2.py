"""
This is Lesson 32. Working with your own object types
Get Programming: Learn to Code with Python
"""

class Stack(object):
    def __init__(self):
        self.stack = []
    def addItem(self, item):
        self.stack.append(item)
    def addManyItems(self, item, number):
        for i in range(number):
            self.stack.append(item)
    def add_list(self, list_to_add):
        for i in range(0, len(list_to_add)):
            item = list_to_add[i]
            self.stack.append(item)
        return self.stack
    def prettyPrint(self):
        for item in self.stack:
            print("*__", item, "__*")


class Pancake(object):
    def __init__(self):
        self.flavour = "chocolate"
    def setFlavour(self, flavour):
        self.flavour = flavour
    def setSize(self, size):
        self.size = size


class Waffle(object):
    def __init__(self):
        self.syrup = "maple"
    def setSyrup(self, syrup):
        self.syrup = syrup


stack_pancakes = Stack()

# The loop creates a new strawberry_pancake object each time it loops
# Each strawberry_pancake object is stored in a different memory location
for i in range(3):
    strawberry_pancake = Pancake()
    strawberry_pancake.setFlavour("stawberry")
    stack_pancakes.addItem(strawberry_pancake)

stack_pancakes.prettyPrint()

caramel_waffle = Waffle()
caramel_waffle.setSyrup("caramel")
stack_waffles = Stack()

# Adding the same caramel_waffle object many times creates only one caramel_waffle object 
# It is stored in one memory location
stack_waffles.addManyItems(caramel_waffle, 5)
stack_waffles.prettyPrint()
