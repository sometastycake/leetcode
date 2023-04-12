# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = defaultdict(int)
        for letter in s:
            counter[letter] += 1
        amounts = list(counter.values())
        for i in range(len(amounts) - 1):
            if amounts[i] != amounts[i + 1]:
                return False
        return True
