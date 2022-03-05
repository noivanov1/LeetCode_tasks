# LeetCode:
# 26.02.2022
# Runtime: 304 ms, faster than 13.82% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.2 MB, less than 56.41% of Python3 online submissions for First Unique Character in a String.

def firstUniqChar(s: str) -> int:
    _dict = {}
    for i in range(len(s)):
        if s[i] not in _dict:
            _dict.update({s[i]: 1})
        else:
            _dict.update({s[i]: _dict.get(s[i]) + 1})
    for key, val in _dict.items():
        if val == 1:
            return s.index(key)
    return -1


s = "loveleetcode"

print(firstUniqChar(s))