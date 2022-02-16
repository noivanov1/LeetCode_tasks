# LeetCode:
# 16.02.2022
# Runtime: 62 ms, faster than 11.26% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.9 MB, less than 86.10% of Python3 online submissions for Number of 1 Bits.

def hammingWeight1(n: int) -> int:
    return bin(n).count('1')


# Runtime: 54 ms, faster than 24.85% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.8 MB, less than 86.10% of Python3 online submissions for Number of 1 Bits

def hammingWeight2(n: int) -> int:
    return bin(n).count('1')




