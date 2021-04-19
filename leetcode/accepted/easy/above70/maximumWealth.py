# Runtime: 52 ms, faster than 72.83% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14.2 MB, less than 59.83% of Python3 online submissions for Richest Customer Wealth.

accounts = [[1,2,3],[3,2,1]]

def maximumWealth():
    highNum = 0

    for i in accounts:
        pHolder = 0

        for j in i:
            pHolder += j
        
        if pHolder > highNum:
            highNum = pHolder
    
    print(highNum)

maximumWealth()

# Runtime: 56 ms, faster than 38.36% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14.4 MB, less than 28.50% of Python3 online submissions for Richest Customer Wealth.

# accounts = [[1,2,3],[3,2,1]]

# def maximumWealth():
#     highNum = 0

#     for i in accounts:
#         if sum(i) > highNum:
#             highNum = sum(i)
    
#     print(highNum)

# maximumWealth()


