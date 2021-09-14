# Runtime: 64 ms, faster than 78.55% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 15.1 MB, less than 19.96% of Python3 online submissions for Maximum Subarray.

nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
    lenNums = len(nums) # Hold nums length
    if lenNums == 1: # Only holds one value
        return nums[0] # Return highest vlaue
    
    sum, max = nums[0], nums[0]

    for i in range (1, lenNums):
        sum += nums[i]

        if nums[i] > sum:
            sum = nums[i]
        
        if sum > max:
            max = sum
    
    return max
