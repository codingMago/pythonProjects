# Runtime: 82 ms, faster than 47.93% of Python3 online submissions for Two Sum.
# Memory Usage: 15.4 MB, less than 20.75% of Python3 online submissions for Two Sum.

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):

    pHolder = {}
    
    for i, j in enumerate(nums):
        remainder = target - j

        if remainder in pHolder:
            return[pHolder[remainder], i]
        
        else:
            pHolder[j] = i
    
    return []


print(twoSum(nums,target))
















        
        # if remainder - 
        # pHolder.append(i)
        

    # for i, j in enumerate(nums):
    #     pHolder.append(j)
    #     remainder = target - j
    #     for a, b in enumerate(pHolder):
    #         if b + remainder == target:
    #             return [pHolder[a], i]
        
    #     pHolder.append(j)

    # return []



