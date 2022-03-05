from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if (target < nums[mid]) and (target >= nums[left]):
                right = mid - 1
            else:
                left = mid + 1
        else:

            if (target > nums[mid]) and (target <= nums[right]):
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0

print(search(nums, target))
