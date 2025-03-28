from typing import List


def removeDuplicates( nums: List[int]) -> int:

    i = 1
    j = 1
    existing_duplicate = False
    prev = nums[0]

    while j < len(nums):

        curr = nums[j]

        if curr != prev:
            existing_duplicate = False
            nums[i] = nums[j]
            prev = curr
            i+=1
            j+=1

        elif existing_duplicate:
            j+=1

        else:
            nums[i] = nums[j]
            existing_duplicate = True
            i+=1
            j+=1


    return i





a = [0,1,1,1,1,1,1,1,1]

print(removeDuplicates((a)))
print(a)