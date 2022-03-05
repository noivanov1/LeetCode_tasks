# LeetCode:
# 18.02.2022
# Runtime: 203 ms, faster than 77.62% of Python3 online submissions for Reverse String.
# Memory Usage: 18.4 MB, less than 93.30% of Python3 online submissions for Reverse String.


from typing import List


def reverseString(s: List[str]) -> None:
    n = len(s)
    for i in range( n//2):
        s[i], s[ n - i -1] = s[ n - i -1], s[i]


s = ["h","e","l","l","o"]
print(reverseString(s))