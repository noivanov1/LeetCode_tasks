# LeetCode:
# 16.02.2022
# Runtime: 218 ms, faster than 51.36% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 97.17% of Python3 online submissions for Majority Element.



from typing import List


def majorityElement(nums: List[int]) -> int:
    _dict = {}
    for elem in nums:
        if elem not in _dict:
            _dict.update({elem: 1})
        else:
            _dict.update({elem: _dict.get(elem) + 1})
    return max(_dict.items(), key=lambda k_v: k_v[1])[0]


nums = [2,2,1,1,1,2,2]

print(majorityElement(nums))


