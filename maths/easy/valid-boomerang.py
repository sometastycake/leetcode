# https://leetcode.com/problems/valid-boomerang/

import math
from typing import List


class Solution:

    def distanceBetweenTwoPoints(self, xi: int, yi: int, xj: int, yj: int) -> float:
        return math.sqrt(pow(xj - xi, 2) + pow(yj - yi, 2))

    def isBoomerang(self, points: List[List[int]]) -> bool:
        f = points[0]
        s = points[1]
        t = points[2]
        a = self.distanceBetweenTwoPoints(f[0], f[1], s[0], s[1])
        b = self.distanceBetweenTwoPoints(f[0], f[1], t[0], t[1])
        c = self.distanceBetweenTwoPoints(s[0], s[1], t[0], t[1])
        p = (a + b + c) / 2
        p1 = p * (p - a) * (p - b) * (p - c)
        if p1 <= 0:
            return False
        s = math.sqrt(p1)
        return s > 0.001
