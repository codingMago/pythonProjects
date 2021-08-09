nums = [8,1,2,3,1,1,4]

def smallerNumbersThanCurrent(nums):
    arrLength = len(nums)
    holderArray = []
   
    while len(holderArray) != arrLength:

        for i in range(len(nums)):
            currNum = nums.pop(i)
            counter = 0

            for j in range(len(nums)):
                if nums[j] < currNum:
                    counter += 1
        
            nums = nums[:i] + [currNum] + nums[i:] # Recreate the array
            holderArray.append(counter)
    
    return holderArray

print(smallerNumbersThanCurrent(nums))


# Runtime: 468 ms, faster than 18.41% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 14.5 MB, less than 14.35% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

# nums = [8,1,2,3,1,1,4]

# def smallerNumbersThanCurrent(nums):
#     arrLength = len(nums)
#     holderArray = []
   
#     while len(holderArray) != arrLength:

#         for i in range(len(nums)):
#             currNum = nums.pop(i)
#             counter = 0

#             for j in range(len(nums)):
#                 if nums[j] < currNum:
#                     counter += 1
        
#             nums = nums[:i] + [currNum] + nums[i:] # Recreate the array
#             holderArray.append(counter)
    
#     return holderArray

# print(smallerNumbersThanCurrent(nums))
    
        
        

