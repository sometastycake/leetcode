# https://leetcode.com/problems/surface-area-of-3d-shapes/

from typing import List


class Solution:

    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                value = grid[i][j]
                if value == 0:
                    continue
                cubesurface = 2
                for x, y in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    coord_i = i + x
                    coord_j = j + y
                    if coord_i == -1 or coord_j == -1 or coord_i == n or coord_j == n:
                        cubesurface += value
                    else:
                        neighbor = grid[coord_i][coord_j]
                        if value > neighbor:
                            cubesurface += value - neighbor
                surface += cubesurface
        return surface
