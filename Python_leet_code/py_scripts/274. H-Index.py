


def hIndex( citations) -> int:


    citations.sort(reverse=True)

    i = 0
    curr_max = 0
    while i < len(citations):
        if citations[i] > i:
            curr_max = i+1
        elif citations[i] <= i+1:
            break
        i+=1

    return curr_max

print(hIndex([3,0,6,1,5]))
