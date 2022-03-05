# LeetCode:
# 24.02.2022
# Runtime: 32 ms, faster than 88.41% of Python3 online submissions for Ugly Number.
# Memory Usage: 13.8 MB, less than 82.45% of Python3 online submissions for Ugly Number.


def isUgly(n: int) -> bool:
    s = n
    while s != 0:
        s = 0
        if n % 3 == 0:
            s = int(n / 3)
            n = s
        if n % 2 == 0:
            s = int(n / 2)
            n = s
        if n % 5 == 0:
            s = int(n / 5)
            n = s
    if n != 1:
        return False
    return True


n = 6
print(isUgly(n))