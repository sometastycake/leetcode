# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        idir, jdir = 0, 1
        direction = 'top'
        offset = 0
        i, j = 0, -1
        for _ in range(rows * cols):
            i += idir
            j += jdir
            result.append(matrix[i][j])
            if i == offset and j == cols - offset - 1 and direction == 'top':
                direction = 'down'
                idir, jdir = 1, 0
            elif i == rows - offset - 1 and j == cols - offset - 1 and direction == 'down':
                direction = 'left'
                idir, jdir = 0, -1
            elif i == rows - offset - 1 and j == offset and direction == 'left':
                direction = 'top'
                idir, jdir = -1, 0
            elif i == offset + 1 and j == offset and direction != 'down':
                idir, jdir = 0, 1
                offset += 1
        return result
