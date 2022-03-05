# LeetCode:
# 24.02.2022
# Runtime: 65 ms, faster than 16.84% of Python3 online submissions for Happy Number.
# Memory Usage: 13.8 MB, less than 99.00% of Python3 online submissions for Happy Number.

def isHappy(n: int) -> bool:
    s = 0
    j = 0
    while s != 1:
        s = 0
        for i in str(n):
            s += int(i) ** 2
            n = s
        j += 1
        if j > 10:
            return False
    return True


n = 19
print(isHappy(n))