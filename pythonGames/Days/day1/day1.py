# print("Hello user, what's your name?")
# x = input()
# print("Two integral variable pls? One first")
# a = input()
# a = int(a)
# print("Second one pls?")
# b = input()
# b = int(b)

# add = a+b
# sub = a-b
# div = a/b
# mult = a * b
# outprintstring = f"Add, {add}. Subtract, {sub}. Divide, {div}. Multiply, {mult}."
# print(outprintstring)
import random

def randoNumGen(num, initial, final):
    for a in range(num):
        print(random.randint(initial, final))

# randoNumGen(1, 0, 10)

def swapValues(a, b):
    c = a
    a = b
    b = c

    print(f"a: {a}, b: {b}")

swapValues(10, 50)