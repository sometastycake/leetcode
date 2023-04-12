# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            j = n - 1
            while j >= 0 > grid[i][j]:
                result += 1
                j -= 1
            i += 1
        return result
