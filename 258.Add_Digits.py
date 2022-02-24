# LeetCode:
# 24.02.2022
# Runtime: 36 ms, faster than 82.02% of Python3 online submissions for Add Digits.
# Memory Usage: 13.8 MB, less than 96.89% of Python3 online submissions for Add Digits.

def addDigits(num: int) -> int:
    while len(str(num)) > 1:
        s = 0
        for i in str(num):
            s += int(i)
        num = s
    return num


num = 38
print(addDigits(num))