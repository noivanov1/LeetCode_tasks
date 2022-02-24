# LeetCode:
# 24.02.2022
# Runtime: 26 ms, faster than 93.83% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.9 MB, less than 92.37% of Python3 online submissions for Length of Last Word.

def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))