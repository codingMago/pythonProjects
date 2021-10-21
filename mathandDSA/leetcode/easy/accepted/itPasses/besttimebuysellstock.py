prices = [7,1,5,3,6,4]

def maxProfit(prices):
    max_profit = 0
    high_buy = 0

    prices = prices[::-1]

    for price in prices:
        if price > high_buy:
            high_buy = price
        if high_buy - price > max_profit:
            max_profit = high_buy - price
    
    return max_profit

print(maxProfit(prices))

# Runtime: 1446 ms, faster than 15.55% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.2 MB, less than 52.28% of Python3 online submissions for Best Time to Buy and Sell Stock.

# prices = [7,1,5,3,6,4]

# def maxProfit(prices):
#     max_profit = 0
#     high_buy = 0

#     prices = prices[::-1]

#     for price in prices:
#         if price > high_buy:
#             high_buy = price
#         if high_buy - price > max_profit:
#             max_profit = high_buy - price
    
#     return max_profit