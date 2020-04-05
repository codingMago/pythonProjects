import random


# print("Hello World!")


# def hitCard():
#     return(str(random.randrange(2, 11)))

class playerUser:
    playerPoints = 0
    initialCards = []


    def hitCard(self):
        return(str(random.randrange(2, 11)))

    def gamePrinter(self):
        playerUser.initialCards.append(self.hitCard()) # Give player initial card 0
        playerUser.initialCards.append(self.hitCard()) # Give player initial card 1
        print("Welcome to Manny's Blackjack program!")
        print("You get a " + playerUser.initialCards[0] + " and a " + playerUser.initialCards[1])
        print(self.initialCards)

p = playerUser()

p.gamePrinter()











# class GameLogic:
#     playerPoints, dealerPoints = 0 # Keep Score of points

#     # Trackers Below
#     playerHitCounter = 0 # Simple statistic to keep track of

#     # Every call will provide new card values