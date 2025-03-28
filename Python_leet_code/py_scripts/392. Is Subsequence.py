

def isSubsequence( s: str, t: str):
    i = 0

    for l in t:
        if i > len(s) - 1:
            break


        print(f" l {l}")


        print(f"  l == s[i] { l == s[i]}")
        if l == s[i]:
            i += 1

    print(f" i {i}")

    return i == len(s)



print(isSubsequence("b", "c"))