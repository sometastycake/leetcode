# https://leetcode.com/problems/largest-local-values-in-a-matrix/

from typing import List


class Solution:

    def max(self, grid: List[List[int]], i: int, j: int) -> int:
        result = 0
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                if grid[x][y] > result:
                    result = grid[x][y]
        return result

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []
        i = 0
        while i + 3 <= n:
            j = 0
            row = []
            while j + 3 <= n:
                row.append(self.max(grid, i, j))
                j += 1
            result.append(row)
            i += 1
        return result
