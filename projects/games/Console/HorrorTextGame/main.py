import os 
from os import system 
import time 
from time import sleep 
import sys 
from player import Player
from tools import Tools




black = "\033[0;30m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"





def scrollingText(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def clearScreen():
    system('clear')


user = Player()
print(red)
scrollingText("The Haunting\n\nA psychological thriller built with love and hope\nEnjoy the experience, see you on the other side!\n\n\n-E")
time.sleep(3)
clearScreen()
scrollingText("Please choose a username: ")
clearScreen()
user.userName = input()
scrollingText(f"{user.userName}?\n0) As weak as a baby \n1) Stronger than a toddler \n2) I can cook my own meals \n3) I'll fight when needed \n4) Here to save others\n\n")
if int(input()):
    user.fearLevel = int(input())
    clearScreen()
else:
    print("Invalid number")
    time.sleep(.4)




if user.fearLevel == 0:
    print(white)
    scrollingText("It's been a long drive through what you can only make out as blue with passing green patches, you feel tingling on your stomach and just can't make out the feeling")
    print("0) Cry\n1) Laugh\n2) Sleep")

    if int(input()):
        print("hello world!")
        
elif user.fearLevel == 1:
    pholder = ""
elif user.fearLevel == 2:
    print(blue)
    scrollingText("You awaken at the shallow end of a lake. Where are you? How'd you get there? \n")
    time.sleep(1)

    print("1. Look for other survivors | 2. Scavenge for resources | 3. Yell for a response | 4. Refuse to accept the circumstances and sleep \nChoice: ")
    firstAction = input()

    if firstAction == '1':
        print(green)
        scrollingText("Behind a set of trees and further into the thick of the forest you spot a fire.")
        time.sleep(1)

    elif firstAction == '2':
        print(green)
        scrollingText("After some searching you find a sharp rock")

    elif firstAction == '3':
        print(red)
        scrollingText("You begin to")

    elif firstAction == '4':
        print(red)
        scrollingText("The cold harsh climate weakens you, you're awakened to growls and see beady luminescent eyes focused on you.")
        user.hitPoints -= 40
        
elif user.fearLevel == 4:
    ppjads = ""

else:
    print("Invalid Action")


# x = input("1. Go back to sleep, 2. Say pog")

# if x == "1":
#   scrollingText("You went back to sleep.")

# elif x == "2":
#   print(red)
#   scrollingText("You died lol")

# else:
#   scrollingText("Invalid argument")