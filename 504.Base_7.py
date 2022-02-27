# LeetCode:
# 16.02.2022
# Runtime: 58 ms, faster than 17.36% of Python3 online submissions for Base 7.
# Memory Usage: 13.8 MB, less than 82.30% of Python3 online submissions for Base 7.
# Test:
# if num = 0
# return '0'

# if num = -10
# return -13


def convertToBase7(num: int) -> str:
    if num == 0:
        return '0'
    if num < 0:
        num *= -1
        sign = '-'
    else:
        sign = ''
    b = ''
    while num > 0:
        b = str(num % 7) + b
        num = num // 7
    return sign + b