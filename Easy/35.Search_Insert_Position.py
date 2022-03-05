# LeetCode:
# 24.02.2022
# Runtime: 66 ms, faster than 55.46% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.6 MB, less than 94.17% of Python3 online submissions for Search Insert Position.

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target not in nums:
        for i in range(len(nums)):
            if target < nums[i]:
                return i
        return len(nums)
    return nums.index(target)

nums = [1,3,4,5]
target = 2
print(searchInsert(nums, target))