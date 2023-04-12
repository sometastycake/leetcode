# https://leetcode.com/problems/convert-1d-array-into-2d-array/

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n > len(original):
            return []
        result = []
        i = 0
        rowscounter = 0
        while i < len(original):
            if rowscounter >= m:
                return []
            result.append(original[i: i + n])
            i += n
            rowscounter += 1
        return result
