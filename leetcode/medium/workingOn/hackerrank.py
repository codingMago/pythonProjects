simulations = ["C","R","U","L"]

def minChairs(simulations):
    minChairs = 0 # Chairs total needed
    currChairs = 0 # Keep track of chairs available

    x = len(simulations)
    while x != 0: # Loop through simulations

        if i == "C" or "U":
            if currChairs >= 1:
                    currChairs -= 1
            else:
                minChairs += 1
                
        elif i == "R" or "L":
            currChairs += 1

        else:
            return 0
        x -= 1
        

    return minChairs # Return how many chairs we have to buy

x = "CRULLURCRC"
print(minChairs(x))