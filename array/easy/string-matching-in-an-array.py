# https://leetcode.com/problems/string-matching-in-an-array/

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        sortedWords = list(sorted(words, key=lambda word: len(word)))
        for i in range(len(sortedWords) - 1):
            for j in range(i + 1, len(sortedWords)):
                if sortedWords[i] in sortedWords[j]:
                    result.append(sortedWords[i])
                    break
        return result
