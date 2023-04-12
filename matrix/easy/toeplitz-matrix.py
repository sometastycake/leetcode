# https://leetcode.com/problems/toeplitz-matrix/

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            for j in range(0, n):
                x, y = i - 1, j - 1
                if x >= 0 and y >= 0 and matrix[i][j] != matrix[x][y]:
                    return False
        return True
