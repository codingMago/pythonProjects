# Runtime: 32 ms, faster than 93.22% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 14.3 MB, less than 22.57% of Python3 online submissions for Kids With the Greatest Number of Candies.

candies = [1, 2, 3, 4, 2, 1]
extraCandies = 2

def kidsWithCandies():
    highNum = 0
    pHolder = []
    for i in candies:
        if i > highNum:
            highNum = i

    for i in candies:
        if i + extraCandies >= highNum:
            pHolder.append(True)
        else:
            pHolder.append(False)
    
    return pHolder

print(kidsWithCandies())


