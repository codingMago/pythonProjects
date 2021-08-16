nums = [3,2,1]

def thirdMax(nums):
        nums = sorted(nums)
        
        if len(nums) < 3:
            return nums.pop()

        else:
            nums.pop()
            nums.pop()
        
        return nums.pop()


print(thirdMax(nums))