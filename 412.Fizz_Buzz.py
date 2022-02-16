# LeetCode:
# 16.02.2022
# Runtime: 62 ms, faster than 43.59% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 14.9 MB, less than 98.69% of Python3 online submissions for Fizz Buzz.


from typing import List


def fizzBuzz(n: int) -> List[str]:
    new_list = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            new_list.append("FizzBuzz")
        elif i % 3 == 0:
            new_list.append("Fizz")
        elif i % 5 == 0:
            new_list.append("Buzz")
        else:
            new_list.append(str(i))
    return new_list


n = 15
print(fizzBuzz(n))
