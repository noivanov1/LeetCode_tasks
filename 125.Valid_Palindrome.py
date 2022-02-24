# LeetCode:
# 18.02.2022
# Runtime: 70 ms, faster than 44.19% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.1 MB, less than 34.91% of Python3 online submissions for Valid Palindrome.


def isPalindrome(s: str) -> bool:
    if len(s) == 1 or s == ' ':
        return True
    new_s = ''.join([item for item in s.lower() if item.isalnum()])
    if new_s == new_s[::-1]:
        return True
    return False

n = '.,'
print(isPalindrome(n))