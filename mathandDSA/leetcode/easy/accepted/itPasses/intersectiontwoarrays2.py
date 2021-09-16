# Runtime: 106 ms, faster than 6.75% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.5 MB, less than 41.33% of Python3 online submissions for Intersection of Two Arrays II.
nums1 = [1,2,2,1]
nums2 = [2,2]

def intersect(nums1, nums2):
    num1len = len(nums1) # Compare array lengths
    num2len = len(nums2)
    pHolder = [] # Hold unto return values

    if num1len >= num2len: # If first array larger than second or equivalent
        for i in nums2: # Work on current value of smaller array
            if i in nums1: # If that value is found in bigger array
                pHolder.append(i) # Append value to return array
                nums1.remove(i) # Remove that value from the bigger array
    else: # Second array larger than first
        for i in nums1: # Work on current value of smaller array
            if i in nums2: # If that value is found in bigger array
                pHolder.append(i) # Append value to return array
                nums2.remove(i) # Remove that value from the bigger array


    return pHolder # Return array with intersections

print(intersect(nums1, nums2))
