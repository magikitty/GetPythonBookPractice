"""
This is Lesson 32. Working with your own object types
Get Programming: Learn to Code with Python
"""

class Queue(object):
    def __init__(self):
        self.queue = []
    def length_queue(self):
        print("There are", len(self.queue), "people in the queue")
    def add_person(self, person):
        self.queue.append(person)
    def add_many_people(self, person, number):
        for _ in range(number):
            self.queue.append(person)
    def remove_person(self):
        self.queue.pop(0)
    def remove_many_people(self, number):
        for _ in range(0, number):
            counter = 0
            self.queue.pop(counter)
            counter += 1
    def pretty_print(self):
        for person in self.queue:
            print("--", person, "--")


# Testing method calls
store_queue = Queue()
store_queue.add_person("Billy Bob")
store_queue.add_many_people("Jane", 3)
store_queue.add_many_people("May", 2)
store_queue.remove_person()
store_queue.add_person("Lulu")
store_queue.pretty_print()

store_queue.remove_many_people(4)
store_queue.length_queue()
store_queue.pretty_print()
