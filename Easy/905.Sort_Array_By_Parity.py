# LeetCode:
# 17.02.2022
# Runtime: 129 ms, faster than 31.54% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.7 MB, less than 88.52% of Python3 online submissions for Sort Array By Parity.


from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    odds = []
    even = []
    for x in nums:
        if x % 2 != 0:
            odds.append(x)
        else:
            even.append(x)
    return even + odds


nums = [3,1,2,4]
print(sortArrayByParity(nums))