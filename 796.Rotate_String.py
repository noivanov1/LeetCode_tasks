# LeetCode:
# 17.02.2022
# Runtime: 32 ms, faster than 78.60% of Python3 online submissions for Rotate String.
# Memory Usage: 14 MB, less than 73.74% of Python3 online submissions for Rotate String.


def rotateString(s: str, goal: str) -> bool:
    new_s = ''
    for _ in range(len(s) + 1):
        if s == goal:
            return True
        new_s = s[1:len(s)] + s[0:1]
        s = new_s
    return False


s = "abcde"
goal = "cdeab"

print(rotateString(s, goal))