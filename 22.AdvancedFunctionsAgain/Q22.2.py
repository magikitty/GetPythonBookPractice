"""
This is Lesson 22: Advanced operations with functions
Get Programming: Learn to Code With Python
"""
# Q 22.2

def person(age):
    print("I am a person")
    def student(major):
        print("I like learning")
        def vacation(place):
            print("But I need to take breaks")
            print(age, "/", major, "/", place)
        return vacation
    return student

person(29)("CS")("Japan")
person(23)("Law")("Florida")
person(244)("Cats")("Snowy mountain top")