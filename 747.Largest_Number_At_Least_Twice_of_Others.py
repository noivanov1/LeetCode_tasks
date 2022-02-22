# LeetCode:
# 22.02.2022
# Runtime: 65 ms, faster than 19.60% of Python3 online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 13.9 MB, less than 83.80% of Python3 online submissions for Largest Number At Least Twice of Others.

from typing import List


def dominantIndex(nums: List[int]) -> int:
    max = nums[0]
    for item in nums:
        if max < item:
            max = item
    for item in nums:
        if max / 2 < item and max != item:
            return -1
    return nums.index(max)

nums = [3,6,1,0]

print(dominantIndex(nums))