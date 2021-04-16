# Runtime: 36 ms, faster than 84.76% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.5 MB, less than 43.91% of Python3 online submissions for Running Sum of 1d Array.

nums = [1, 2, 3, 4]

def runningSum():
    runNum = 0

    for i, j in enumerate(nums):
        runNum += j
        nums[i] = runNum
    
    return nums

runningSum()

