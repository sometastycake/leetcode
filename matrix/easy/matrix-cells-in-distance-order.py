# https://leetcode.com/problems/matrix-cells-in-distance-order/

from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        coords = []
        for i in range(rows):
            for j in range(cols):
                coords.append({'i': i, 'j': j, 'd': abs(rCenter - i) + abs(cCenter - j)})
        coords = sorted(coords, key=lambda v: v['d'])
        return [[v['i'], v['j']] for v in coords]
