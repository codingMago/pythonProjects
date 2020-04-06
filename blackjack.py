import random


class gameLogic:
    # TODO: Move game functionality here

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

    def gamePrinter(self):
        print("Welcome to Manny's Blackjack program!")
        print("You get a " + str(player.playerCards[0]) + " and a " + str(player.playerCards[1]))
        print("Your total is " + str(sum(player.playerCards)))
        print("The dealer has a {} showing, and a hidden card", )
        print(player.playerCards)

        

class player:
    # Player attributes
    playerCards = [random.randrange(2,11), random.randrange(2,11)] #Holds player cards, points can be figured out on the spot, initialized to provide 2 first cards

    # Player functionality
    def hitCard(self):
        self.playerCards.append(random.randrange(2,11))
        if sum(playerCards) == 21:
            print("Blackjack! You win!")
        if sum(playerCards) > 21:
            print("House wins! Your score: " + str(sum(playerCards)))

        print(self.playerCards)


class dealer:
    # Dealer attributes
    delearCards = [random.randrange(2,11), random.randrange(2,11)] #Holds dealer cards, points can be figured out on the spot, initialized to provide 2 first cards

    # Dealer functionality
    def hitCard(self):
        self.dealerCards.append(random.randrange(2,11))
        if sum(dealerCards) == 21:
            print("Blackjack! You win!")
        if sum(dealerCards) > 21:
            print("Player wins! House scored: " + str(sum(dealerCards)))

        print(self.dealerCards)
    # Dealer can hit on <= 16
    # if dealer.points > 21:
    #   player Wins

# Test game
p = player()
p.hitCard()

# NOTES
# Dealer and player seem to need their own hitCard function, seeing as the dealer will have certain constraints that the player won't
# i.e: dealer won't be hitting anything if they have more than 16 points whereas player can wing it