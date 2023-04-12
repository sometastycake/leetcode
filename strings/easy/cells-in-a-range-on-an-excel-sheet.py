# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphabet = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        result = []
        beginColumn = alphabet.index(s[0])
        endColumn = alphabet.index(s[3])
        beginRow = int(s[1])
        endRow = int(s[4])
        for column in range(beginColumn, endColumn + 1):
            for row in range(beginRow, endRow + 1):
                result.append(f'{alphabet[column]}{row}')
        return result
