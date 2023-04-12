# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

from collections import defaultdict
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        colsmaxvalue = defaultdict(int)
        rowsminvalue = defaultdict(lambda: 999999)
        rowsmincolindex = defaultdict(int)
        for i in range(m):
            index = 0
            for j in range(n):
                if matrix[i][j] > colsmaxvalue[j]:
                    colsmaxvalue[j] = matrix[i][j]
                if matrix[i][j] < rowsminvalue[i]:
                    rowsminvalue[i] = matrix[i][j]
                    index = j
            rowsmincolindex[rowsminvalue[i]] = index
        result = []
        for rowindex, minvalue in rowsminvalue.items():
            colindex = rowsmincolindex[minvalue]
            maxvalue = colsmaxvalue[colindex]
            if maxvalue == minvalue:
                result.append(minvalue)
        return result
