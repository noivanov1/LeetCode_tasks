# LeetCode:
# 05.03.2022
# Runtime: 42 ms, faster than 53.13% of Python3 online submissions for Number Complement.
# Memory Usage: 13.8 MB, less than 74.89% of Python3 online submissions for Number Complement.

# Test:
# if num = 5
# return 2


def findComplement(num: int) -> int:
    _num = ''
    for i in str("{0:b}".format(num)):

        if i == '0' :
            _num += '1'
        else:
            _num += '0'

    return int(_num ,2)


num = 5
print(findComplement(num))