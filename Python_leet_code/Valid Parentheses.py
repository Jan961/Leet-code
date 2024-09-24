


def isValid(self, s: str) -> bool:
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for i in range(len(s)):
        bracket = s[i]

        if bracket in brackets.keys():
            stack.append(brackets[bracket])
        else:
            if len(stack) == 0 or stack[-1] != bracket:
                return False
            else:
                stack.pop()

    return stack == []