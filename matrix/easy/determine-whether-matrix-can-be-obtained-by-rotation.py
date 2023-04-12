# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

from typing import List


class Solution:

    def rotate(self, mat: List[List[int]]):
        n = len(mat)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                tmp = mat[i][j]
                mat[i][j] = mat[n - j - 1][i]
                mat[n - j - 1][i] = mat[n - i - 1][n - j - 1]
                mat[n - i - 1][n - j - 1] = mat[j][n - i - 1]
                mat[j][n - i - 1] = tmp

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        k = 0
        while k < 3 and mat != target:
            self.rotate(mat)
            k += 1
        return mat == target
