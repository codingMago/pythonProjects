from Classes.user import User

# Put in a counter of users, to see what user of the app is currently in. We're gonna have to input FILE I/O
# for eachUser in UserLog.txt
#   create and load next user
# return User
User1 = User()





def helloWorld(statement): # 1-1 && 1-2
    print(f"Here's your statement: {statement}")

def getNameAge(UserNumber): # 1-3


    userInput = input(f"Alpha001: Username: ")
    if userInput:
        if len(userInput) > 10:
            "Alpha001: Shorter Username: "
            # Needs reset of input functionality

        UserNumber.userName = userInput

        


    age = input(f'Alpha001: Age: ')
    if age:
        age = int(age) 
        age *= 365

        # make note of user ageif age > 100
    
    UserNumber.userAge = str(age)

    return UserNumber

def getUserInput():
    return(input())

User1 = getNameAge(User1)
print(f"User's age: {User1.userAge}, User's Name: {User1.userName} ")