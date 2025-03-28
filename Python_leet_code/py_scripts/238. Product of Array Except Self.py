


def productExceptSelf( nums):

    out = []

    prev = 1
    for i in range(len(nums) -1):
        curr = nums[i]*prev
        out.append(curr)
        prev = curr
    out.append(out[-1])

    print(f" out {out}")

    prev = 1
    for i in range(len(nums)-2, 0, -1):
        b = nums[i+1]*prev
        out[i]= b*out[i-1]
        prev = b
        print(f"prev", prev)

    out[0] = prev*nums[1]

    return out


print(productExceptSelf( [-1,1,0,-3,3]))