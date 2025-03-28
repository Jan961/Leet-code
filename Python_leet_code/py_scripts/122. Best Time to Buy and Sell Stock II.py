from collections import defaultdict
from typing import List


def maxProfit( prices: List[int]) -> int:

    i = 0
    j = 1
    total_profit = 0
    curr_largest_profit = 0

    while j < len(prices):

        if prices[j-1] <= prices[j]:
            curr_largest_profit = prices[j] - prices[i]
            j+=1
        else:

            if curr_largest_profit  >= 0 :
                total_profit += curr_largest_profit
                curr_largest_profit = 0
            i = j
            j+=1

    total_profit += curr_largest_profit

    return total_profit


print(maxProfit([7,6,4,3,1]))