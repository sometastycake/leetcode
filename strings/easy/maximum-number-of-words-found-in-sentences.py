# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for sentence in sentences:
            amount = len(sentence.split(' '))
            if amount > result:
                result = amount
        return result
