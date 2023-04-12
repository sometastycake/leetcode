# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

import math
from typing import List


class Solution:

    def distance(self, dx: int, dy: int) -> float:
        return math.sqrt(pow(dx, 2) + pow(dy, 2))

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for xi, yi, radius in queries:
            c = 0
            for xj, yj in points:
                dx = xi - xj
                dy = yi - yj
                if abs(dx) > radius or abs(dy) > radius:
                    continue
                d = self.distance(dx, dy)
                if d <= radius:
                    c += 1
            result.append(c)
        return result
