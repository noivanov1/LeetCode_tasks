# LeetCode:
# 17.02.2022
# Runtime: 289 ms, faster than 56.18% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.1 MB, less than 64.86% of Python3 online submissions for Squares of a Sorted Array.


from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    new_l = [ x *x for x in nums]
    new_l.sort()
    return new_l


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))