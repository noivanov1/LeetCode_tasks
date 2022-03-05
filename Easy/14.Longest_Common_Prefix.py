# LeetCode:
# 24.02.2022
# Runtime: 68 ms, faster than 13.95% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14 MB, less than 79.41% of Python3 online submissions for Longest Common Prefix.


from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    j = 0
    prefix = ''
    try:
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if strs[0][j] != strs[i][j]:
                    return prefix
            prefix += strs[0][j]
    except IndexError:
        return prefix
    return prefix


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))