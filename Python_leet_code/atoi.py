


def myAtoi(self, s: str) -> int:
    out = 0
    if not len(s):
        return out

    first_digit = 0
    sign = 1

    while (first_digit < len(s)):
        if s[first_digit] == ' ':
            first_digit += 1


    if s[first_digit] == '-':
        sign *= -1
        first_digit += 1
    elif s[first_digit] == "+":
        first_digit +=1

    check_clamp = False if len(s[first_digit:]) >= 10 else True

    pow = 0
    for i in range(len(s) -1 , first_digit-1, -1):
        integer = int(s[i])
        out_new = out + (10**pow)*integer

        if (out_new - oull)



