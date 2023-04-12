# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cache = set()
        result = 0
        for pattern in patterns:
            if pattern in cache:
                result += 1
            elif pattern in word:
                result += 1
                cache.add(pattern)
        return result
