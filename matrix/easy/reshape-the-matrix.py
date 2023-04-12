# https://leetcode.com/problems/reshape-the-matrix/

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        rc = r * c
        mn = m * n
        if rc > mn or rc < mn:
            return mat
        result = []
        row = []
        remaining = c
        for i in range(m):
            j = 0
            while j < n:
                subarray = mat[i][j: j + remaining]
                row += subarray
                j += remaining
                remaining -= len(subarray)
                if len(row) == c:
                    result.append(row)
                    row = []
                    remaining = c
        return result
