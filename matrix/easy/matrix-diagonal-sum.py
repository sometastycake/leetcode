# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        n = len(mat)
        evennumber = not n % 2
        for i in range(n):
            result += mat[i][i]
            result += mat[i][n - i - 1]
        if not evennumber:
            result -= mat[n // 2][n // 2]
        return result
