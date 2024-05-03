import os
# import name
# # # os.system
# # name.namer("sneha")
# name.add(34,54)
# name.product(34,54)
# name.factorial(5)
import name
print(name.x)

# aliasing through as keyword
import name as math
print(math.x)
math.add(345,567)

import name

print(dir(name))# check all the elements inside it

def f1():
    if __name__ == '__main__':#name
        print("the code is executed as a program")
    else:
        print("as a module")
import name
f1()