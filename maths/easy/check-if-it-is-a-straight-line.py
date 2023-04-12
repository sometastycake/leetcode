# https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xi, yi = coordinates[0]
        xj, yj = coordinates[1]
        try:
            r = (xj - xi) / (yj - yi)
        except ZeroDivisionError:
            result = False
        else:
            result = True
        resultByX = True
        resultByY = True
        for i in range(len(coordinates) - 1):
            xi, yi = coordinates[i]
            xj, yj = coordinates[i + 1]
            if result:
                try:
                    result &= r == (xj - xi) / (yj - yi)
                except ZeroDivisionError:
                    result = False
            resultByX &= xi == xj
            resultByY &= yi == yj
            if not result and not resultByX and not resultByY:
                return False
        return True
