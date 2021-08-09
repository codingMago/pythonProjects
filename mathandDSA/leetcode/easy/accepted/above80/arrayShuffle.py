# Runtime: 56 ms, faster than 84.59% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.3 MB, less than 77.20% of Python3 online submissions for Shuffle the Array.

nums = [2, 5, 1, 3, 4, 7]
n = 3

def shuffle(nums, n):
    firHolder = []
    pHolder = 0

    for i in nums:

        if pHolder <= n-1:
            firHolder.append(i)
            firHolder.append(nums[pHolder+n])
        else:
            break

        pHolder += 1
    
    print(firHolder)

shuffle(nums, n)


# Runtime: 60 ms, faster than 61.41% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.4 MB, less than 49.65% of Python3 online submissions for Shuffle the Array.

# nums = [1, 1, 2, 2]
# n = 2

# def shuffle(nums, n):
#     firHolder = []

#     for i, j in enumerate(nums):
#         if i <= n-1:
#             firHolder.append(j)
#             firHolder.append(nums[i+n])
#         else:
#             break
    
#     print(firHolder)

# shuffle(nums, n)


# Runtime: 64 ms, faster than 22.38% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.3 MB, less than 77.15% of Python3 online submissions for Shuffle the Array.

# nums = [1, 1, 2, 2]
# n = 2

# def shuffle(nums, n):
#     firHolder = []
#     secHolder = []

#     for i in nums:
#         if len(firHolder) < n:
#             firHolder.append(i)
#         else:
#             secHolder.append(i)
    
#     nums = []

#     for i in range(len(firHolder)):
#         nums.append(firHolder[i])
#         nums.append(secHolder[i])
    
#     print(nums)

# shuffle(nums, n)