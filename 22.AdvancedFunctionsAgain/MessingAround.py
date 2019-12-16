# A function that initializes a variable
def func_1():
    v = 5
    print(v)

v = 1
func_1()

# A function that accesses a variable outside its scope
def func_2():
    print(lucky_num)

lucky_num = 7
func_2()

# A function that accesses more than one variable outside its scope
def func_3():
    print(num1 + num2)

num1 = 10
num2 = 15
func_3()

# A function that tries to modify a variable defined outside its scope - results in an ERROR
# def not_working():
#     a += 2

# a = 4
# not_working() 