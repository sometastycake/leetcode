# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from typing import List
from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = defaultdict(int)
        words2 = defaultdict(int)
        i, j = 0, 0
        word1 = ''
        word2 = ''
        while i < len(s1) or j < len(s2):
            if i < len(s1):
                if s1[i] != ' ':
                    word1 += s1[i]
                else:
                    words1[word1] += 1
                    word1 = ''
                i += 1
            if j < len(s2):
                if s2[j] != ' ':
                    word2 += s2[j]
                else:
                    words2[word2] += 1
                    word2 = ''
                j += 1
        if word1:
            words1[word1] += 1
        if word2:
            words2[word2] += 1
        result = []
        for word, amount in words1.items():
            if amount == 1 and word not in words2:
                result.append(word)
        for word, amount in words2.items():
            if amount == 1 and word not in words1:
                result.append(word)
        return result
