import random


def coinflip(amount, min=None, max=None):
    if min == None or max == None:
        while amount != 0:
            x = random.randint(0, 1)
            if x == 1:
                print(f"{x}: Heads!")
            else:
                print(f"{x}: Tails!")
            amount -= 1

    else:
        while amount != 0:
            x = random.randint(min, max)
            if x % 2 == 0:
                print(f"{x}: Even! ..I mean heads!")
            else:
                print(f"{x}: Odd? Tails!")
            amount -= 1

# coinflip(10)
# print("I love pancakes")
# coinflip(4, 0, 20)

def getUserInfo():
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: 0 = Female, 1 = Male: ")

    if int(gender) == 1:
        print(f"Mr.{name}")
    else:
        print(f"Ms.{name}")

    if name == "Blabla":
        print("Cool name!")

# getUserInfo()

def shakeEightBall():
    x = random.randint(0, 3)

    if x == 0:
        print("HELLO!")
    elif x == 1:
        print("SAUSAGE")
    elif x == 2:
        print("Orange")
    elif x == 3:
        print("Apples")

shakeEightBall()