# https://leetcode.com/problems/transpose-matrix/

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        if m == n:
            for i in range(n - 1):
                for j in range(i, n):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp
            return matrix
        else:
            result = []
            for i in range(n):
                row = []
                for j in range(m):
                    row.append(matrix[j][i])
                result.append(row)
            return result
