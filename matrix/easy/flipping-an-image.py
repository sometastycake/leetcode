# https://leetcode.com/problems/flipping-an-image/

from typing import List


class Solution:

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(image)
        for array in image:
            row = array[::-1]
            i = 0
            j = n - 1
            while i <= j:
                row[i] = 1 if row[i] == 0 else 0
                if i < j:
                    row[j] = 1 if row[j] == 0 else 0
                i += 1
                j -= 1
            result.append(row)
        return result
