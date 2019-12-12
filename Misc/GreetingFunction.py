"""
Example of calling a function from another function
"""

# Function definitions
def greet(nameToGreet):
    print("Hellow " + nameToGreet)

def greetNumberOfTimes(nameToGreet, numberTimesToGreet):

    counter = 0
    while counter < numberTimesToGreet:
        greet(nameToGreet)
        counter+=1


# Function executions
greetNumberOfTimes("bob", 3)
