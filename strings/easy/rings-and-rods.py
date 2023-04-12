# https://leetcode.com/problems/rings-and-rods/

from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        i = 0
        rods = defaultdict(set)
        while i < n:
            color = rings[i]
            rod = rings[i + 1]
            rods[rod].add(color)
            i += 2
        result = 0
        for colors in rods.values():
            if len(colors) == 3:
                result += 1
        return result
