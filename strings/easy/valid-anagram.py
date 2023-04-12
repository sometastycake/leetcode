# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = Counter(s)
        for letter in t:
            if letter not in counter:
                return False
            counter[letter] -= 1
        return all(not value for value in counter.values())
