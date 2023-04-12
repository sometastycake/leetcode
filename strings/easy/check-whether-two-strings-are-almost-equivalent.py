# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        for letter, amount in counter2.items():
            if abs(counter1[letter] - amount) > 3:
                return False
        for letter, amount in counter1.items():
            if abs(counter2[letter] - amount) > 3:
                return False
        return True
