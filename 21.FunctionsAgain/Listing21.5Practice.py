# Function with and without a return

def return_thing(thing):
    return thing 

def print_message(message):
    print(message + "\nFuck off mate, all you get is this message!")

return_thing("ball")   # print nothing (return "ball")
print_message("Hello!")  # print "Hello! Fuck off mate, all you get is this message" (return None)
print(return_thing("mat"))  # print "mat" (return "mat")
print(print_message("Gimme my ball back!")) # print "Gimme my ball back! Fuck off mate, all you get is this message", print None
