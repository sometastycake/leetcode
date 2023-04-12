# https://leetcode.com/problems/count-prefixes-of-a-given-string/

from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        result = 0
        for word in words:
            if s.startswith(word):
                result += 1
        return result
