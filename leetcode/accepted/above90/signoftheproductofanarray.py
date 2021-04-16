# Runtime: 56 ms, faster than 91.26% of Python3 online submissions for Sign of the Product of an Array.
# Memory Usage: 14.3 MB, less than 70.36% of Python3 online submissions for Sign of the Product of an Array.

arrNums = [1, 5, 0, 2, -3]

def arraySign(nums) -> int:
        product = 1
        
        for i in nums:
            product *= i
        
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0

print(arraySign(arrNums))

# x = "Sign of the Product of an Array"
# x = x.replace(" ", "")
# x = x.lower()
# print(x)