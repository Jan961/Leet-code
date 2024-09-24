from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    common = strs[0]
    end_common = len(strs[0])

    index = 1
    while end_common>0 and index < len(strs):
        j =0
        while j<len(common[:end_common])\
            and j<len(strs[index])\
            and common[j] == strs[index][j]:
            j +=1
        end_common = j
        index +=1

    return common[:end_common]


