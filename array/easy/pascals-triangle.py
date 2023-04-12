# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            array = [1]
            for j in range(0, len(result[i - 1]) - 1):
                array.append(result[i - 1][j] + result[i - 1][j + 1])
            array.append(1)
            result.append(array)
        return result
