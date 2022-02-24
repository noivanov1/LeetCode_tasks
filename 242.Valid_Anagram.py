# LeetCode:
# 24.02.2022
# Runtime: 1930 ms, faster than 5.01% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15 MB, less than 20.45% of Python3 online submissions for Valid Anagram.

def isAnagram(s: str, t: str) -> bool:
    new_t = [item for item in t]
    for i in s:
        if i in new_t:
            new_t.remove(i)
        else:
            return False
    if len(new_t) > 0:
        return False
    return True


s = "anagram"
t = "nagaram"

print(isAnagram(s,t))