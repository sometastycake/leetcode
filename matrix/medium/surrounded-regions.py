# https://leetcode.com/problems/surrounded-regions/

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        areas = []
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X' or (i, j) in visited:
                    continue
                queue = [(i, j)]
                area = []
                while queue:
                    x, y = queue.pop(0)
                    if (x, y) in visited:
                        continue
                    area.append((x, y))
                    visited.add((x, y))
                    if x - 1 >= 0 and board[x - 1][y] == 'O' and (x - 1, y) not in visited:
                        queue.append((x - 1, y))
                    if y + 1 < len(board[x]) and board[x][y + 1] == 'O' and (x, y + 1) not in visited:
                        queue.append((x, y + 1))
                    if x + 1 < len(board) and board[x + 1][y] == 'O' and (x + 1, y) not in visited:
                        queue.append((x + 1, y))
                    if y - 1 >= 0 and board[x][y - 1] == 'O' and (x, y - 1) not in visited:
                        queue.append((x, y - 1))
                if area:
                    areas.append(area)
        for area in areas:
            is_surrounded_area = True
            for coordinates in area:
                x, y = coordinates
                if x == 0 or y == 0 or x == len(board) - 1 or y == len(board[x]) - 1:
                    is_surrounded_area = False
                    break
            if is_surrounded_area:
                for coordinates in area:
                    x, y = coordinates
                    board[x][y] = 'X'
