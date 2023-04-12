# https://leetcode.com/problems/available-captures-for-rook/

from collections import defaultdict
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        figuresByRows = defaultdict(list)
        figuresByCols = defaultdict(list)
        for i in range(8):
            for j in range(8):
                figure = board[i][j]
                if figure == '.':
                    continue
                if board[i][j] in ('p', 'B'):
                    figuresByRows[i].append(figure)
                    figuresByCols[j].append(figure)
                    continue
                attacked = 0
                if i in figuresByRows and figuresByRows[i][-1] == 'p':
                    attacked += 1
                if j in figuresByCols and figuresByCols[j][-1] == 'p':
                    attacked += 1
                for k in range(j + 1, 8):
                    if board[i][k] == 'p':
                        attacked += 1
                        break
                    if board[i][k] == 'B':
                        break
                for k in range(i + 1, 8):
                    if board[k][j] == 'p':
                        attacked += 1
                        break
                    if board[k][j] == 'B':
                        break
                return attacked
        return 0
