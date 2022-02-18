# LeetCode:
# 18.02.2022
# Runtime: 28 ms, faster than 96.47% of Python3 online submissions for Add Binary.
# Memory Usage: 13.9 MB, less than 84.97% of Python3 online submissions for Add Binary.


def addBinary(a: str, b: str) -> str:
    aa = int(a, 2)
    bb = int(b ,2)
    return bin(aa +bb)[2:]

a = '11'
b = '1'
print(addBinary(a,b))