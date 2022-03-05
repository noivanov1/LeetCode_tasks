from typing import List


def Sum_Two_2for(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def Sum_Two_hash(nums: List[int], target: int) -> List[int]:
    map_hash = {}
    for i in range(len(nums)):
        if target - nums[i] in map_hash:
            return [i, map_hash[target - nums[i]]]
        map_hash[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print(Sum_Two_hash(nums, target))
print(Sum_Two_2for(nums, target))
