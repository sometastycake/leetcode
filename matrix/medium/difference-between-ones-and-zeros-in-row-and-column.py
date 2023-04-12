# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

from collections import defaultdict
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onesRow = defaultdict(int)
        onesCol = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
        for i in range(m):
            zeros = m - onesRow[i]
            preValue = onesRow[i] - zeros
            for j in range(n):
                grid[i][j] = preValue + onesCol[j] - (n - onesCol[j])
        return grid
