import math

def isEven(number):
    if number % 2 == 0:
        print(True)
    else:
        print(False)

def FtoC(fahrenheit):
    celsius = (fahrenheit -32.0) * (5.0/9.0)

    print(celsius)

def findHypotenuse(a, b):
    hypo = (a*a) + (b*b)
    hypo = math.sqrt(hypo)

    print(hypo)

def findGrade(grade):
    if grade >= 90 and grade <= 100:
        print('A')
    elif grade >= 80 and grade < 90:
        print('B')
    elif grade >= 73 and grade < 80:
        print('C')
    elif grade >= 70 and grade < 73:
        print('D')
    else:
        print('?')
