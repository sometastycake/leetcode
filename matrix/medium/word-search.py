# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != word[0]:
                    continue
                queue = [(i, j, 0)]
                visited = []
                while queue:
                    x, y, index = queue.pop()
                    if index <= len(visited):
                        visited = visited[:index]
                    if (x, y) not in visited:
                        visited.append((x, y))
                        if index == len(word) - 1:
                            return True
                        if x - 1 >= 0 and board[x - 1][y] == word[index + 1]:
                            queue.append((x - 1, y, index + 1))
                        if y + 1 < cols and board[x][y + 1] == word[index + 1]:
                            queue.append((x, y + 1, index + 1))
                        if x + 1 < rows and board[x + 1][y] == word[index + 1]:
                            queue.append((x + 1, y, index + 1))
                        if y - 1 >= 0 and board[x][y - 1] == word[index + 1]:
                            queue.append((x, y - 1, index + 1))
        return False
