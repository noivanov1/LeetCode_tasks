# LeetCode:
# 18.02.2022
# Runtime: 898 ms, faster than 41.49% of Python3 online submissions for Arranging Coins.
# Memory Usage: 13.8 MB, less than 98.93% of Python3 online submissions for Arranging Coins.


def arrangeCoins(n: int) -> int:
    i = 0
    while i < n:
        i += 1
        n -= i
    return i

n = 5
print(arrangeCoins(n))