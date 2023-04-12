# https://leetcode.com/problems/find-the-difference/

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS = Counter(s)
        result = ''
        for letter in t:
            if not counterS[letter]:
                result += letter
            else:
                counterS[letter] -= 1
        return result
