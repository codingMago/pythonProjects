
# nums = [1,2,3,1]

# def containsDuplicate(nums) -> bool:
    
#     try:
#         set = set(nums)
#     except:
#         return True
    
#     return False

# print(containsDuplicate(nums))

# Runtime: 124 ms, faster than 49.08% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.7 MB, less than 95.61% of Python3 online submissions for Contains Duplicate.

# nums = [1,2,3,1]

# def containsDuplicate(nums) -> bool:
    
#     nums = sorted(nums)
#     numlen = len(nums)
#     previous = nums[0]

#     for i in range(1, numlen):
#         if nums[i] == previous:
#             return True
#         previous = nums[i]
    
#     return False

# print(containsDuplicate(nums))

# Runtime: 128 ms, faster than 36.71% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.7 MB, less than 95.61% of Python3 online submissions for Contains Duplicate.

# nums = [1,2,3,1]

# def containsDuplicate(nums) -> bool:
    
#     previous = -999999999
#     nums = sorted(nums)
#     numlen = len(nums)

#     for i in range(0, numlen):
#         if nums[i] == previous:
#             return True
#         previous = nums[i]
    
#     return False

# print(containsDuplicate(nums))

# Runtime: 194 ms, faster than 11.52% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 19 MB, less than 89.56% of Python3 online submissions for Contains Duplicate.
# nums = [1,2,3,1]

# def containsDuplicate(nums) -> bool:
    

#     previous = -999999999
#     nums = sorted(nums)

#     for i in nums:
#         if i == previous:
#             return True
#         previous = i
    
#     return False

# print(containsDuplicate(nums))

# def containsDuplicate(nums) -> bool:
    
#     pHolder = []
#     for i in nums:
#         if i in pHolder:
#             return True
#         pHolder.append(i)
    
#     return False


# def containsDuplicate(nums) -> bool:
    
#     pHolder = []
#     for i in range(0, len(nums)):
#         if nums[i] in pHolder:
#             return True
#         pHolder.append(nums[i])
    
#     return False






