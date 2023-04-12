# https://leetcode.com/problems/positions-of-large-groups/

from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        i = 0
        while i < len(s) - 1:
            k = i
            while i < len(s) - 1 and s[i] == s[i + 1]:
                i += 1
            if k == i:
                i += 1
                continue
            if i - k + 1 >= 3:
                result.append([k, i])
        return result
