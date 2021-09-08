# Runtime: 52 ms, faster than 43.10% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15 MB, less than 56.12% of Python3 online submissions for Search Insert Position.

nums = [1,3,5,6]
target = 5

def searchInsert(nums, target: int) -> int:
    pHolder = 0
    counter = 0

        
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
        elif target > nums[i]:
            pHolder = i+1
    
    return pHolder

print(searchInsert(nums, target))