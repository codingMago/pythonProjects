
scenarios = ["10", "2", "5"]

def maximumContainers(scenarios):
    # Assign each integer from the string to n, cost, m
    n, cost, m = scenarios # Unpack variables
    budget = int(n) # Budget
    containerPrice = int(cost) # Container price
    tradeIn = int(m) # Trade-In
    currentContainers = 0 # How many we're holding
    totalContainers = 0 # Total we've been able to collect

    def purchaseContainer():
        currentContainers += budget // cost
        totalContainers += currentContainers
        budget -= cost

    def returnContainer():
        while currentContainers >= tradeIn:
            currentContainers -= tradeIn
            totalContainers += 1

    purchaseContainer()
        
    while currentContainers >= tradeIn:
        returnContainer()
    
    print(totalContainers)  

maximumContainers(scenarios)