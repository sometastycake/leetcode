# https://leetcode.com/problems/find-common-characters/


from collections import defaultdict
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lettersCounter = defaultdict(set)
        minLettersCounter = defaultdict(lambda : 999)
        for i, word in enumerate(words):
            currentLettersCounter = defaultdict(int)
            for letter in word:
                lettersCounter[letter].add(i)
                currentLettersCounter[letter] += 1
            for letter, amount in currentLettersCounter.items():
                if amount < minLettersCounter[letter]:
                    minLettersCounter[letter] = amount
        result = []
        for letter, wordIndexes in lettersCounter.items():
            if len(wordIndexes) != len(words):
                continue
            result += [letter] * minLettersCounter[letter]
        return result
