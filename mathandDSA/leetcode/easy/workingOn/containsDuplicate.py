# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums = [1,2,3,4]

def containsDuplicate(nums) -> bool:
    
    pHolder = []
    for i in nums:
        if i in pHolder:
            return True
        pHolder.append(i)
    
    return False


print(containsDuplicate(nums))