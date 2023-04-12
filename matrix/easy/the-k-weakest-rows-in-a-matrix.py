# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        soldiers = []
        for i in range(m):
            j = 0
            while j < n and mat[i][j] == 1:
                j += 1
            soldiers.append((i, j))
        soldiers = sorted(soldiers, key=lambda item: item[1])
        result = []
        for item in soldiers[:k]:
            result.append(item[0])
        return result
