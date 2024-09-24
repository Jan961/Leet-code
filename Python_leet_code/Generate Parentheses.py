from typing import List
from collections import deque


def generateParenthesis( n: int) -> List[str]:

    out_arr = []

    def create_string(n, to_close, position, string_arr, output_arr):
        if position == 2*n :
            output_arr.append(string_arr)

        elif( to_close == 2*n - position ):
            string_arr.append(')')
            create_string(n, to_close - 1, position + 1,string_arr, output_arr)
        else:
            if (to_close == 0):
                string_arr.append('(')
                create_string(n, to_close + 1, position + 1, string_arr, output_arr)
            else:
                new_arr = string_arr.copy()
                new_arr.append('(')
                string_arr.append(')')
                create_string(n, to_close + 1, position + 1, new_arr, output_arr)
                create_string(n, to_close - 1, position + 1, string_arr, output_arr)

    create_string(n,0,0,[],out_arr)
    for i in range(len(out_arr)):
        out_arr[i] = "".join(out_arr[i])
    return out_arr


print(generateParenthesis(3))



