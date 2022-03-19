# LeetCode:
# 19.03.2022
# Runtime: 30 ms, faster than 89.60% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
# Memory Usage: 13.8 MB, less than 65.61% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
#
# Test:


# if n = 11
# return [2,9]


from typing import List


def getNoZeroIntegers(n: int) -> List[int]:
    i = 1
    while True:
        if str(n - i).count('0') == 0 and str(i).count('0') == 0:
            return [i, n - i]
        i += 1


n = 2
print(getNoZeroIntegers(n))