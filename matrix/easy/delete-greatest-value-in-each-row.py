# https://leetcode.com/problems/delete-greatest-value-in-each-row

from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i, array in enumerate(grid):
            grid[i] = list(sorted(array, reverse=True))
        result = 0
        m = len(grid)
        n = len(grid[0])
        for _ in range(n):
            local_max = 0
            for i in range(m):
                if grid[i][0] > local_max:
                    local_max = grid[i][0]
                grid[i] = grid[i][1:]
            result += local_max
        return result
