# LeetCode:
# 18.02.2022
# Runtime: 88 ms, faster than 49.00% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.9 MB, less than 71.14% of Python3 online submissions for Palindrome Number.

def isPalindrome(x: int) -> bool:
    for i in range(len(str(x)) // 2 + 1):
        if str(x)[i] != str(x)[-i - 1]:
            return False
    return True


x = 121
print(isPalindrome(x))
