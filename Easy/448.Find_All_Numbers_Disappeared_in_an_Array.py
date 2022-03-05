# LeetCode:
# 16.02.2022
# Runtime: 410 ms, faster than 68.45% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 26.2 MB, less than 10.15% of Python3 online submissions for Find All Numbers Disappeared in an Array.

# Test:
# if nums = [1,1]
# return [2]


from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n_nums = [i for i in range(1, len(nums) + 1)]
    return [i for i in set(n_nums).difference(set(nums))]

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))