# LeetCode:
# 19.03.2022
# Runtime: 72 ms, faster than 57.79% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 13.9 MB, less than 90.06% of Python3 online submissions for Find Numbers with Even Number of Digits.
#
# Test:
# if num = 0
# return '0'

# if nums = [555,901,482,1771]
# return 1


from typing import List


def findNumbers(nums: List[int]) -> int:
    return len([item for item in nums if len(str(item)) % 2 == 0])


nums = [12,345,2,6,7896]
print(findNumbers(nums))