



def strStr( haystack: str, needle: str) -> int:
    hi = 0
    hi_end = len(haystack) - len(needle) + 1
    ni_end = len(needle)
    found = -1
    while hi < hi_end:
        if haystack[hi] == needle[0]:
            print(found)
            found = hi
            hci = hi
            ni = 0
            while hci < len(haystack) and ni < ni_end and haystack[hci] == needle[ni]:
                print(hci)
                hci += 1
                ni += 1
            if ni == ni_end:
                return found
            else:
                found = -1
        hi += 1

    return found



print(strStr("mississippi", "issip"))
