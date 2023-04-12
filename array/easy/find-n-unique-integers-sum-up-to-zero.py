# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        values = list(range(1, n // 2 + 1))
        negativeValues = list(map(lambda value: value * (-1), values))
        if not n % 2:
            return negativeValues + values
        return negativeValues + [0] + values
