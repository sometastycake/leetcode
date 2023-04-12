# https://leetcode.com/problems/largest-triangle-area/

import math
from typing import List


class Solution:

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        for i in range(len(points) - 2):
            xi, yi = points[i]
            for j in range(i + 1, len(points) - 1):
                xj, yj = points[j]
                a = math.sqrt(pow(xj - xi, 2) + pow(yj - yi, 2))
                if not a:
                    continue
                for k in range(j + 1, len(points)):
                    xk, yk = points[k]
                    if xi == xj == xk or yi == yj == yk:
                        continue
                    b = math.sqrt(pow(xk - xi, 2) + pow(yk - yi, 2))
                    if not b:
                        continue
                    c = math.sqrt(pow(xj - xk, 2) + pow(yj - yk, 2))
                    if not c:
                        continue
                    p = (a + b + c) / 2
                    p1 = p * (p - a) * (p - b) * (p - c)
                    if p1 < 0:
                        continue
                    s = math.sqrt(p1)
                    if s > maxArea:
                        maxArea = s
        return round(maxArea, 6)
