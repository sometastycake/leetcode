# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

import math
from collections import defaultdict
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        cols = defaultdict(set)
        rows = defaultdict(set)
        sumcols = defaultdict(int)
        sumrows = defaultdict(int)
        sm = int(math.fsum(range(1, n + 1)))
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                if val in rows[i] or val in cols[j]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                sumrows[i] += val
                sumcols[j] += val
                if sumrows[i] > sm or sumcols[j] > sm:
                    return False
        return True
