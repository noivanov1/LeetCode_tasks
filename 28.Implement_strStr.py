# LeetCode:
# 24.02.2022
# Runtime: 35 ms, faster than 88.97% of Python3 online submissions for Implement strStr().
# Memory Usage: 14.1 MB, less than 82.11% of Python3 online submissions for Implement strStr().


def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    return -1


haystack = "hello"
needle = "ll"

print(strStr(haystack, needle))