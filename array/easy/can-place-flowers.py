# https://leetcode.com/problems/can-place-flowers/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            return False
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i] == 1:
                continue
            if f[i - 1] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
            if n == 0:
                return True
        return n == 0
