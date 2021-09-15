nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


def merge(nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m:]
        nums2 = nums2[:n:]
        nums1[:] = sorted(nums1 + nums2)

        # nums1[:] = sorted(nums1[:m:] + nums2)
        # [start:stop:format]
        # nums1 = nums1[]
        print(nums1)

merge(nums1, m, nums2, n)