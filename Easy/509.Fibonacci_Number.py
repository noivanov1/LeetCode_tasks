# LeetCode:
# 17.02.2022
# 48 ms, Your runtime beats 98.15 % of python3 submissions.
# Memory Usage: 13.8 MB, less than 86.90% of Python3 online submissions for Fibonacci Number.


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    F = [0, 1]
    for i in range(2, n+ 1):
        F.append(F[i - 2] + F[i - 1])
    return F[n]


n = 4
print(fib[n])