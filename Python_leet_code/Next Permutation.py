from typing import List



def nextPermutation(nums: List[int]) -> None:
    i = len(nums) - 2
    prev = nums[i + 1]

    while (i >= 0 and nums[i] >= prev):
        prev = nums[i]
        i -=1


    if i == -1:
        nums.sort()
    else:
        j_s = len(nums) - 1
        while nums[j_s] <= nums[i]:
            j_s -=1

        temp = nums[j_s]
        nums[j_s] = nums[i]
        nums[i] = temp

        nums[i+1:] = sorted(nums[i+1:])




a = [1,3,2]
nextPermutation(a)
print(a)

