# https://leetcode.com/problems/shift-2d-grid/

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        lastcol = []
        for i in range(m):
            lastcol.append(grid[i][n - 1])
        for _ in range(k):
            for i in range(m):
                for j in range(n - 1, 0, -1):
                    grid[i][j] = grid[i][j - 1]
            grid[0][0] = lastcol[-1]
            for j in range(0, m - 1):
                grid[j + 1][0] = lastcol[j]
            for i in range(m):
                lastcol[i] = grid[i][n - 1]
        return grid
