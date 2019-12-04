# 1. Initialise variables
num = int(input("Enter a number: "))
counter = num

# 2. Iterate through num range
for i in range(num):

    if counter > 1:
        print(counter, "Python books on the shelf", counter, "Python books. "
              "Take one down, pass it around,", counter - 1,
              "books left.")

    else:
        print(counter, "Python book on the shelf", counter,
              "book on Python. "
              "Take one down, pass it around, no more books!")
    counter -= 1
