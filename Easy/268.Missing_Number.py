# LeetCode:
# 24.02.2022
# Runtime: 140 ms, faster than 80.83% of Python3 online submissions for Missing Number.
# Memory Usage: 15.3 MB, less than 69.80% of Python3 online submissions for Missing Number.

from typing import List


def missingNumber(nums: List[int]) -> int:
    nums.sort()
    try:
        for i in range(len(nums) + 1):
            if i != nums[i]:
                return i
    except IndexError:
        return i

nums = [3,0,1]
print(missingNumber(nums))