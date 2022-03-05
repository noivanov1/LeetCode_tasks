# LeetCode:
# 05.03.2022
# Runtime: 765 ms, faster than 9.34% of Python3 online submissions for Relative Ranks.
# Memory Usage: 15.2 MB, less than 66.96% of Python3 online submissions for Relative Ranks.


# Test:
# if score = [5,4,3,2,1]
# return ["Gold Medal","Silver Medal","Bronze Medal","4","5"]


from typing import List


def findRelativeRanks(score: List[int]) -> List[str]:
    rank = ['0'] * len(score)
    titles = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + [str(i + 4) for i in range(len(score) - 2)]
    _dict = {item: value for value, item in enumerate(score)}
    for i in range(len(score)):
        _max = max(_dict)
        rank[_dict.get(_max)] = titles[i]
        _dict.pop(_max)
    return rank


score = [10,3,8,9,4]
print(findRelativeRanks(score))