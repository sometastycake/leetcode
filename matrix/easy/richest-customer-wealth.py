# https://leetcode.com/problems/richest-customer-wealth/

import math
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        n = len(accounts[0])
        for array in accounts:
            amount = int(math.fsum(array))
            if amount > result:
                result = amount
            elif amount == n * 100:
                return n * 100
        return result
