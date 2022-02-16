def isPalindrome(x: int) -> bool:
    for i in range(len(str(x)) // 2 + 1):
        if str(x)[i] != str(x)[-i - 1]:
            return False
    return True


x = 121
print(isPalindrome(x))
