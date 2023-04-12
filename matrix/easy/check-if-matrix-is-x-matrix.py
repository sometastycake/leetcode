# https://leetcode.com/problems/check-if-matrix-is-x-matrix/

from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j:
                    if grid[i][j] == 0:
                        return False
                elif j == n - i - 1:
                    if grid[i][n - i - 1] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False
        return True
