# LeetCode:
# 16.02.2022
# Runtime: 81 ms, faster than 6.35% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.9 MB, less than 43.26% of Python3 online submissions for Find the Difference.


def findTheDifference(s: str, t: str) -> str:
    for item in s:
        new_s = t[:t.index(item)] + t[t.index(item ) +1:]
        t = new_s
    return t


# XOR

# Runtime: 58 ms, faster than 35.34% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.9 MB, less than 43.26% of Python3 online submissions for Find the Difference.

def findTheDifferenceXOR(s: str, t: str) -> str:
    char = 0
    for i in range(len(s)):
        char ^= ord(s[i]) ^ ord(t[i])
    char ^= ord(t[-1])
    return chr(char)


s = "abcd"
t = "abcde"
print(findTheDifference(s, t))
print(findTheDifferenceXOR(s, t))