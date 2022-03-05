# LeetCode:
# 16.02.2022
# Runtime: 41 ms, faster than 54.67% of Python3 online submissions for Reverse Bits.
# Memory Usage: 13.9 MB, less than 69.54% of Python3 online submissions for Reverse Bits.

def reverseBits(n: int) -> int:
    if len(str(n)) != 32:
        str_n = format(n, "b")
    else:
        str_n = str(n)
    s = str_n[::-1]
    while len(s) < 32:
        s += '0'
    return int(s, 2)
