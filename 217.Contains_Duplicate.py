# LeetCode:
# 18.02.2022
# Runtime: 497 ms, faster than 61.48% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 25.9 MB, less than 73.05% of Python3 online submissions for Contains Duplicate.

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    original = {}
    for i in range(len(nums)):
        if nums[i] in original:
            return True
        else:
            original[nums[i]] = i
    return False