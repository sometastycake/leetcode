# https://leetcode.com/problems/matrix-block-sum/

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        result = []
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            row = []
            for j in range(n):
                rowStart = i - k
                colStart = j - k
                if rowStart < 0:
                    rowStart = 0
                if colStart < 0:
                    colStart = 0
                rowEnd = i + k
                colEnd = j + k
                if rowEnd >= m:
                    rowEnd = m - 1
                if colEnd >= n:
                    colEnd = n - 1
                c = 0
                for ii in range(rowStart, rowEnd + 1):
                    for jj in range(colStart, colEnd + 1):
                        c += mat[ii][jj]
                row.append(c)
            result.append(row)
        return result
