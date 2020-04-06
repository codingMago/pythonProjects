import random


class gameLogic:
    # TODO: Move game functionality here

    def hitCard(self):

        if sum(player.playerCards) > 21:
            print("Dealer wins! You've gone over 21 points. Total: " + str(sum(player.playerCards)))
        if sum(player.playerCards) < 21:
            print("""Would you like to "hit" or "stay"?""")
            # PSEDUOCODE: 
            # if console.readLine() == "hit":
            #   player.playerCards.append(self.hitCard())
            # if console.readLine() == "stay":
            #   if dealer.points <= 16:
            #       dealer.hitCard()    
            #   

        

class player:
    playerCards = [random.randrange(2,11), random.randrange(2,11)] #Holds player cards, points can be figured out on the spot


    def hitCard(self):
        # return(random.randrange(2, 11))
        self.playerCards.append(random.randrange(2,11))
        print(self.playerCards)
        
        

    def gamePrinter(self):
        player.playerCards.append(self.hitCard()) # Give player initial card 0
        player.playerCards.append(self.hitCard()) # Give player initial card 1
        print("Welcome to Manny's Blackjack program!")
        print("You get a " + str(player.playerCards[0]) + " and a " + str(player.playerCards[1]))
        print("Your total is " + str(sum(player.playerCards)))
        print(player.playerCards)

class dealer:
    delearCards = [random.randrange(2,11), random.randrange(2,11)] #Holds dealer cards, points can be figured out on the spot

    # def hitCard(self):

    # Dealer can hit on <= 16
    # if dealer.points > 21:
    #   player Wins

# Test game
p = player()
p.hitCard()

# NOTES
# Dealer and player seem to need their own hitCard function, seeing as the dealer will have certain constraints that the player won't
# i.e: dealer won't be hitting anything if they have more than 16 points whereas player can wing it