'''
Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” 
instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
'''

def fizzBuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz: {i}")
        elif i % 3 == 0:
            print(f"Fizz: {i}")
        elif i % 5 == 0:
            print(f"Buzz: {i}")
        else:
            print(i)

fizzBuzz()