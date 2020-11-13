def prob1():

    try:
        a = input("Hello, user! How old are you?")
        a = int(a)
    except:
        a = input("Numerals ONLY: ")

    finally:

        if int(a) <= 13:
            print("Sorry, user, but you're a bit too young. Buh-bye!")
        elif int(a) >= 13:
            print("Roses are red,")
            print("Silent as a mouse,")
            print("Your door is unlocked.")
            print("I'm inside your house!")
        else:
            print("no")

def intUserInput(userString):
    a = "Tostitos, que rrrrRRRiiico!" # 

    while type(a) != type(1):
        try:
            a = input(userString)
            a = int(a)
        except:
            a = input("Numerals ONLY '1, 2, 3, ...: ")
            a = int(a)
    
    return a

def prob2():
    a = input("Print the hour to convert from Pacific to Eastern: ")
    a = int(a)
    if a <= 12 and a >= 1:
        b = a + 3
        if b > 12:
            b -= 12
        print(f"That would be {b}PM Eastern.")
    else:
        print("Not valid time! (1-24)")
    
prob2()