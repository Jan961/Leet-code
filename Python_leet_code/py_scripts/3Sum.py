from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    out = []
    nums.sort()
    i = 0

    while i < len(nums):
        curr = nums[i]
        if curr > 0:
            break
        if i > 0 and curr == nums[i - 1]:
            i += 1
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            nl = nums[l]
            nr = nums[r]
            sum = curr + nl + nr

            if sum == 0:
                out.append([curr, nr, nl])
                l += 1
                r -= 1
                while r < len(nums) - 1 and r > l and nums[r] == nums[r + 1]:
                    r -= 1
                while l > i + 1 and r > l and nums[l] == nums[l - 1]:
                    l += 1

            elif sum < 0:
                l += 1
            else:
                r -= 1

        i += 1

    return out


print(threeSum([-1,0,1,2,-1,-4]))