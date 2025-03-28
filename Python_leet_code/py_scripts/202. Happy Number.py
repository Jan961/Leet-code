from typing import List


def isHappy(self, n: int):


    def check(n, prev: List[int]):

        if n in prev:
            return False

        else:
            digits = [int(d) for d in str(n)]

            if sum(digits) == 1:
                return True
            else:
                prev.append(n)
                return check(sum([d**2 for d in digits]), prev)

    return check(n, [])



