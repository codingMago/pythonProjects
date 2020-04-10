import random



class player:
    # Player attributes
    playerCards = [random.randrange(2,11), random.randrange(2,11)] #Holds player cards, points can be figured out on the spot, initialized to provide 2 first cards

    # Player functionality
    def getCards(self):
        return self.playerCards
        # print(self.playerCards)
    def hitCard(self):
        self.playerCards.append(random.randrange(2,11))
        # if sum(self.playerCards) == 21:
        #     print("Blackjack! You win!")
        # if sum(self.playerCards) > 21:
        #     print("House wins! Your score: " + str(sum(playerCards)))

        # print(self.playerCards)

class dealer:
    # Dealer attributes
    delearCards = [random.randrange(2,11), random.randrange(2,11)] #Holds dealer cards, points can be figured out on the spot, initialized to provide 2 first cards

    # Dealer functionality
    def hitCard(self):
        self.dealerCards.append(random.randrange(2,11))
        # if sum(dealerCards) == 21:
        #     print("Blackjack! You win!")
        # if sum(dealerCards) > 21:
        #     print("Player wins! House scored: " + str(sum(dealerCards)))
    # Dealer can hit on <= 16
    # if dealer.points > 21:
    #   player Wins

class gameLogic:
    # TODO: Move game functionality here

    blablaguy = player()
    pTotal = sum(blablaguy.playerCards)
    dealer0 = dealer()
    # dTotal = sum(dealer0.dealerCards)

    def gamePrinter(self):
        print("Welcome to Manny's Blackjack program!")
        print("You get an " + str(self.blablaguy.playerCards[0]) + " and a " 
        + str(self.blablaguy.playerCards[1]) + ". Total: " + str(self.pTotal))
        print("The dealer has a " + str(self.dealer0.delearCards[0]) + " showing, and a hidden card")

        while self.pTotal < 21:
            userChoice = input("""Would you like to "H"it or "S"tay?""")

            if userChoice == "H" or userChoice == "h":
                self.blablaguy.hitCard()

            elif userChoice == "S" or userChoice == "s":
                print("Your current total: " + str(self.pTotal))

        # Pseudocode for implementing reading user input
        # if
        # print(self.blablaguy.playerCards)

    # if sum(self.blablaguy.playerCards) > 21:
    #     print("Dealer wins! You've gone over 21 points. Total: " + str(sum(self.blablaguy.playerCards)))
    # if sum(self.blablaguy.playerCards) < 21:
    #     print("""Would you like to "hit" or "stay"?""")
        # PSEDUOCODE: 
        # if console.readLine() == "hit":
        #   player.playerCards.append(self.hitCard())
        # if console.readLine() == "stay":
        #   if dealer.points <= 16:
        #       dealer.hitCard()    
        #   

        

# Test game
# p = player()
# p.getCards()
g = gameLogic()
g.gamePrinter()

# NOTES
# Dealer and player seem to need their own hitCard function, seeing as the dealer will have certain constraints that the player won't
# i.e: dealer won't be hitting anything if they have more than 16 points whereas player can wing it