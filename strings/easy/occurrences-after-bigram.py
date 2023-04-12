# https://leetcode.com/problems/occurrences-after-bigram/

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        words = text.split(' ')
        if len(words) < 3:
            return []
        i = 0
        while i < len(words) - 2:
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])
            i += 1
        return result
