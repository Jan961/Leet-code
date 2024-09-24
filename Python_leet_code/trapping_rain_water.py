from typing import List


def trap(height: List[int]) -> int:

    total = 0
    l = len(height)

    left_maxes = []
    max_left = height[0]
    for i in range(1, l - 1):
        curr = height[i]
        if curr > max_left:
            max_left = curr
        left_maxes.append(max_left)

    max_right = height[l - 1]
    right_maxes = []
    for i in range(l - 1, 0, -1):
        curr = height[i]
        if curr > max_right:
            max_right = curr
        right_maxes.insert(0, max_right)
    print(len(height))
    print(len(left_maxes))
    print(len(right_maxes))
    for i in range(1, l - 1):
        fill_mark = max(min(right_maxes[i-1], left_maxes[i-1]) - height[i], 0)
        total += fill_mark

    return total


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))