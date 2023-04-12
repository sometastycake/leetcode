# https://leetcode.com/problems/valid-sudoku

from collections import defaultdict
from typing import List


def subbox_index(index: int) -> int:
    if index < 3:
        return 0
    elif index < 6:
        return 1
    else:
        return 2


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cells = defaultdict(set)
        subboxes = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                value = board[i][j]
                index = (subbox_index(i), subbox_index(j))
                if value in rows[i] or value in cells[j] or value in subboxes[index]:
                    return False
                subboxes[index].add(value)
                rows[i].add(value)
                cells[j].add(value)
        return True
