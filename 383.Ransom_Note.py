# LeetCode:
# 25.02.2022
# Runtime: 198 ms, faster than 5.14% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.4 MB, less than 20.45% of Python3 online submissions for Ransom Note.


def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag = [item for item in magazine]
    k = 0
    for elem in ransomNote:
        if elem in mag:
            mag.remove(elem)
            k += 1
    if len(ransomNote) > k:
        return False
    return True


ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))