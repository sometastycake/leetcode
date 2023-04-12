# https://leetcode.com/problems/three-consecutive-odds/

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        amount = 0
        lastIndex = -1
        for i, value in enumerate(arr):
            if not value % 2:
                continue
            if i == lastIndex + 1:
                lastIndex += 1
                amount += 1
                if amount == 3:
                    return True
            else:
                amount = 1
                lastIndex = i
        return False
