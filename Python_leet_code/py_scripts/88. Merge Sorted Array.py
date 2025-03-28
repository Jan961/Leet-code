from typing import List






def merge( nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """


    i = m - 1
    j = n - 1

    k = m + n - 1

    while k >= 0:
        if (i >= 0 and j >= 0 and nums1[i] >= nums2[j]) or j < 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1





nums1 = [1,2,3,0,0,0]
nums2 =  [2,5,6]

merge(nums1,3,nums2,3)
print(nums1)


