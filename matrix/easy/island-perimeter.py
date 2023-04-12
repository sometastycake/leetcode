# https://leetcode.com/problems/island-perimeter/

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    sides = 0
                    if x == 0 or (x - 1 >= 0 and grid[x - 1][y] == 0):
                        sides += 1
                    if y == 0 or (y - 1 >= 0 and grid[x][y - 1] == 0):
                        sides += 1
                    if x == len(grid) - 1 or (x + 1 < len(grid) and grid[x + 1][y] == 0):
                        sides += 1
                    if y == len(grid[x]) - 1 or (y + 1 < len(grid[x]) and grid[x][y + 1] == 0):
                        sides += 1
                    result += sides
                    if x - 1 >= 0 and grid[x - 1][y] == 1 and (x - 1, y) not in visited:
                        queue.append((x - 1, y))
                    if y - 1 >= 0 and grid[x][y - 1] == 1 and (x, y - 1) not in visited:
                        queue.append((x, y - 1))
                    if x + 1 < len(grid) and grid[x + 1][y] == 1 and (x + 1, y) not in visited:
                        queue.append((x + 1, y))
                    if y + 1 < len(grid[x]) and grid[x][y + 1] == 1 and (x, y + 1) not in visited:
                        queue.append((x, y + 1))
        return result
