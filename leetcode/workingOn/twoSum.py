nums = [2, 7, 11, 15]
target = 9

def twoSum():

    remainder = 0
    pHolder = []
    
    for i in nums:
        remainder = target - i
        
        if remainder - 
        pHolder.append(i)
        

    # for i, j in enumerate(nums):
    #     pHolder.append(j)
    #     remainder = target - j
    #     for a, b in enumerate(pHolder):
    #         if b + remainder == target:
    #             return [pHolder[a], i]
        
    #     pHolder.append(j)

    # return []


print(twoSum())

