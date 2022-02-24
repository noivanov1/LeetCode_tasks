# LeetCode:
# 22.02.2022
# Runtime: 95 ms, faster than 21.58% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.9 MB, less than 71.57% of Python3 online submissions for Self Dividing Numbers.

from typing import List


def selfDividingNumbers(left: int, right: int) -> List[int]:
    _list = []
    for i in range(right - left + 1):
        a = [item for item in str(i+left)]
        print(a)
        if '0' not in a:
            b = [0 for item in a if (i + left) % int(item) == 0]
            if len(b) == len(str(i + left)):
                _list. append(i + left)
    return _list

left = 1
right = 22

print(selfDividingNumbers(left, right))
