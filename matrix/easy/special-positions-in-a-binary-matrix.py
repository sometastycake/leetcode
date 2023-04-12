# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cols = {}
        rows = {}
        result = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                if i in rows or j in cols:
                    if j in cols:
                        if i not in rows:
                            rows[i] = -1
                        if cols[j] != -1:
                            rows[cols[j]] = -1
                            cols[j] = -1
                            result -= 1
                    if i in rows:
                        if j not in cols:
                            cols[j] = -1
                        if rows[i] != -1:
                            cols[rows[i]] = -1
                            rows[i] = -1
                            result -= 1
                else:
                    rows[i] = j
                    cols[j] = i
                    result += 1
        return result
