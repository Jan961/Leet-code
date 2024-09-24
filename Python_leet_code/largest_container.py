from typing import List


def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height)-1
    max_volume = 0

    while l<r:
        lower_h = height[l] if height[l] < height[r] else height[r]
        if (r-l)*lower_h > max_volume:
            max_volume = (r-l)*lower_h


        if height[l] < height[r]:
            l+=1
        else:
            r-=1


    return max_volume



print(maxArea([1,1]))