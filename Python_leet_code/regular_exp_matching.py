def isMatch( s: str, p: str) -> bool:

    ls = len(s)
    lp = len(p)
    dyp = [[False for j in range(lp + 1)] for i in range(ls + 1)]
    dyp[0][0] = True

    for j in range(2,lp+1):
        dyp[0][j] = p[j-1] == '*' and dyp[0][j-2]

    for i in range(1, ls + 1):
        for j in range(1, lp + 1):

            if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                dyp[i][j] = dyp[i - 1][j - 1]

            elif p[j - 1] == "*":
                print(dyp[i - 1][j])
                dyp[i][j] = dyp[i][j - 2] or ((s[i - 1] == p[j - 2] or p[j - 2] == ".") and dyp[i - 1][j])

    return dyp[ls][lp]


print(isMatch("aa", "a*"))

