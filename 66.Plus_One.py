# LeetCode:
# 18.02.2022
# Runtime: 42 ms, faster than 53.35% of Python3 online submissions for Plus One.
# Memory Usage: 13.9 MB, less than 69.38% of Python3 online submissions for Plus One.

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    new_str = ''.join([str(i) for i in digits])
    new_str = str(int(new_str) + 1)
    return [i for i in new_str]

n = [1,2,3]

print(plusOne(n))