# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        rowsnum = len(matrix)
        colsnum = len(matrix[0])
        for i in range(rowsnum):
            for j in range(colsnum):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            for i in range(colsnum):
                matrix[row][i] = 0
        for col in cols:
            for j in range(rowsnum):
                matrix[j][col] = 0
