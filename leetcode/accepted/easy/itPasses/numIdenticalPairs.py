
arr = [1,2,3,1,1,3]

def numIdenticalPairs(nums):
    counter = []

    for i in range(len(nums)):
        
        for j in range(len(nums)):
            if i == j: 
                break
            elif nums[i] == nums[j]:
                    counter.append([i, j])

    print(len(counter))

numIdenticalPairs(arr)


# Runtime: 36 ms, faster than 39.14% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14.3 MB, less than 10.47% of Python3 online submissions for Number of Good Pairs.

# arr = [1,2,3,1,1,3]

# def numIdenticalPairs(nums):
#     counter = []

#     for i in range(len(nums)):
        
#         for j in range(len(nums)):
#             if j == i: 
#                 break
#             if nums[i] == nums[j]:
#                     counter.append([j, i])

#     print(len(counter))

# numIdenticalPairs(arr)


# def numIdenticalPairs(nums):
#     counter = []

#     for i in range(len(nums)):
#         loopHolder = 0
#         currNum = nums.pop(i) ## Essential error
        
#         for j in nums:
            
#             if currNum == j:
#                 counter.append([i, loopHolder+1])
#             loopHolder+= 1

#         nums = nums[:i] + [currNum] + nums[i:] # Recreate the array

#     print(counter)

# numIdenticalPairs(arr)