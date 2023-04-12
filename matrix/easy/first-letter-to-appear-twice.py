# https://leetcode.com/problems/first-letter-to-appear-twice/

from collections import defaultdict


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counter = defaultdict(int)
        for letter in s:
            counter[letter] += 1
            if counter[letter] == 2:
                return letter
