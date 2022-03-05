# LeetCode:
# 25.02.2022
# Runtime: 59 ms, faster than 66.67% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.1 MB, less than 65.76% of Python3 online submissions for Intersection of Two Arrays.

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    nums1 = set(nums1)
    nums2 = set(nums2)

    for i in nums1:
        if i in nums2:
            res.append(i)
    return res


nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))