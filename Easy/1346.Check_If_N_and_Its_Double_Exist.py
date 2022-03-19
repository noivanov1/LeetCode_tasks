# LeetCode:
# 19.03.2022
# Runtime: 71 ms, faster than 65.24% of Python3 online submissions for Check If N and Its Double Exist.
# Memory Usage: 13.9 MB, less than 62.79% of Python3 online submissions for Check If N and Its Double Exist.


# Test:
# if arr = [10,2,5,3]
# return True


from typing import List


def checkIfExist(arr: List[int]) -> bool:
    for i in range(len(arr)):
        double = arr[i] * 2
        if double in arr and i != arr.index(double):
            return True
    return False


arr = [7,1,14,11]
print(checkIfExist(arr))