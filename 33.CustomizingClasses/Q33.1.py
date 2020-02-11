"""
This is Lesson 33. Customizing classes
Get Programming: Learn to Code with Python
"""

class Stack(object):
    def __init__(self):
        self.stack = []
    def addItem(self, item):
        self.stack.append(item)
    def addManyItems(self, item, number):
        for _ in range(number):
            self.stack.append(item)
    def add_list(self, list_to_add):
        for i in range(0, len(list_to_add)):
            item = list_to_add[i]
            self.stack.append(item)
        return self.stack
    def prettyPrint(self):
        for item in self.stack:
            print("*__", item, "__*")
    def __str__(self):
        temp_str = ""
        for item in self.stack:
            temp_str += ("|__" + str(item) + "__|\n")
        return temp_str


class Pancake(object):
    def __init__(self):
        self.flavour = "chocolate"
    def setFlavour(self, flavour):
        self.flavour = flavour
    def __str__(self):
        return "*" + str(self.flavour) + "*"


choco_pancake = Pancake()
strawberry_pancake = Pancake()
strawberry_pancake.setFlavour("strawberry")
pancake_stack = Stack()
pancake_stack.addManyItems(choco_pancake, 7)
pancake_stack.addManyItems(strawberry_pancake, 3)
print(pancake_stack)
# print(pancake_stack.__str__())
# print(Pancake.__str__(choco_pancake))
