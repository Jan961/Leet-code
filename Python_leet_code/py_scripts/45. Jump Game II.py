from typing import List


def jump( nums: List[int]) -> int:

    d = [(0,nums[0],0)]
    l =  len(nums)

    for i in range(1, l):

        smallest = l
        temp = ()
        for t in range(len(d)):
            if d[t][2] < smallest:
                smallest = d[t][2]
                temp = (i,nums[i],d[t][2]+1)

        d[:] = [d[t] for t in range(len(d)) if i-d[t][0] != d[t][1]]

        if nums[i] != 0:
            d.append(temp)
        print(d)

    return d.pop()[-1]







print(jump([3,4,2,3,1,1,1]))