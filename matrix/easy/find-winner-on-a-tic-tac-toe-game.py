# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

from collections import defaultdict
from typing import List


class Solution:

    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = {'X': defaultdict(int), '0': defaultdict(int)}
        cols = {'X': defaultdict(int), '0': defaultdict(int)}
        diag = {'X': {'main': 0, 'sec': 0}, '0': {'main': 0, 'sec': 0}}
        figure = 'X'
        players = {'X': 'A', '0': 'B'}
        for move in moves:
            i, j = move[0], move[1]
            rows[figure][i] += 1
            cols[figure][j] += 1
            if i == j:
                diag[figure]['main'] += 1
                if diag[figure]['main'] == 3:
                    return players[figure]
            if (i, j) in ((0, 2), (1, 1), (2, 0)):
                diag[figure]['sec'] += 1
                if diag[figure]['sec'] == 3:
                    return players[figure]
            if rows[figure][i] == 3 or cols[figure][j] == 3:
                return players[figure]
            figure = 'X' if figure == '0' else '0'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
