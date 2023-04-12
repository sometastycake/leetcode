# https://leetcode.com/problems/projection-area-of-3d-shapes/

from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            maxrow = 0
            maxcol = 0
            for j in range(n):
                if grid[i][j]:
                    area += 1
                if grid[i][j] > maxrow:
                    maxrow = grid[i][j]
                if grid[j][i] > maxcol:
                    maxcol = grid[j][i]
            area += maxrow + maxcol
        return area
