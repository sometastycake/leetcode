# https://leetcode.com/problems/shuffle-string/

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(indices)
        i = 0
        for index in indices:
            result[index] = s[i]
            i += 1
        return ''.join(result)
