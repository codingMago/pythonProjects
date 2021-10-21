nums1 = [1,3]
nums2 = [2]

def findMedianSortedArrays(nums1, nums2):
        
        pHolder = []
        for i in nums1:
            for j in nums2:
                if i > j:
                    pHolder.append(i)
                elif i < j:
                    pHolder.append(j)
                else:
                    pHolder.append(i)
                    pHolder.append(j)
            
        pLen = len(pHolder)
        
        if pLen % 2 == 1:
            return pHolder[(pLen//2)-1]
        else:
            return pHolder[pLen//2]
            
print(findMedianSortedArrays(nums1, nums2))