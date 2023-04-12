# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            row = list(range(n))
            matrix.append(row)
        value = 1
        i, j = 0, -1
        direction = 'top'
        offset = 0
        idir, jdir = 0, 1
        for _ in range(n * n):
            i += idir
            j += jdir
            matrix[i][j] = value
            value += 1
            if i == offset and j == n - offset - 1 and direction == 'top':
                direction = 'down'
                idir, jdir = 1, 0
            elif i == n - offset - 1 and j == n - offset - 1 and direction == 'down':
                direction = 'left'
                idir, jdir = 0, -1
            elif i == n - offset - 1 and j == offset and direction == 'left':
                direction = 'top'
                idir, jdir = -1, 0
            elif i == offset + 1 and j == offset and direction != 'down':
                idir, jdir = 0, 1
                offset += 1
        return matrix
