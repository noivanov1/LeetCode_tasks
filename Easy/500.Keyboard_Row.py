# LeetCode:
# 27.02.2022
# Runtime: 54 ms, faster than 22.39% of Python3 online submissions for Keyboard Row.
# Memory Usage: 13.8 MB, less than 98.96% of Python3 online submissions for Keyboard Row.

# Test:
# if nums = ["omk"]
# return []


from typing import List


def findWords(words: List[str]) -> List[str]:
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    new_list = []
    for item in words:
        for j in rows:
            if set(item.lower()).issubset(set(j)) == True:
                new_list.append(item)
                pass
    return new_list


words = ["Hello","Alaska","Dad","Peace"]
print(findWords(words))