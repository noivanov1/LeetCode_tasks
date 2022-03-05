# LeetCode:
# 24.02.2022
# Runtime: 806 ms, faster than 13.63% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.6 MB, less than 15.19% of Python3 online submissions for Move Zeroes.


from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    for _ in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)


nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)