# LeetCode:
# 24.02.2022
# Runtime: 905 ms, faster than 59.11% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 27.4 MB, less than 99.14% of Python3 online submissions for Maximum Subarray.


from typing import List


def maxSubArray(nums: List[int]) -> int:
    sub, maxSub = nums[0], nums[0]
    for item in nums[1:]:
        sub = max(item, sub + item)
        maxSub = max(maxSub, sub)
    return maxSub


nums = [-2,1,-3,4,-1,2,1,-5,4]