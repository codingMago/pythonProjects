import random


# print("Hello World!")


# def hitCard():
#     return(str(random.randrange(2, 11)))

class player:
    playerPoints = 0
    playerCards = []


    def hitCard(self):
        return(random.randrange(2, 11))

    def gamePrinter(self):
        player.playerCards.append(self.hitCard()) # Give player initial card 0
        player.playerCards.append(self.hitCard()) # Give player initial card 1
        print("Welcome to Manny's Blackjack program!")
        print("You get a " + str(player.playerCards[0]) + " and a " + str(player.playerCards[1]))
        print("Your total is " + str(sum(player.playerCards)))
        print(player.playerCards)

class dealer:
    dealerPoints = 0
    delearCards = []



p = player()

p.gamePrinter()











# class GameLogic:
#     playerPoints, dealerPoints = 0 # Keep Score of points

#     # Trackers Below
#     playerHitCounter = 0 # Simple statistic to keep track of

#     # Every call will provide new card values