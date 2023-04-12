# https://leetcode.com/problems/single-number/

from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for value, amount in counter.items():
            if amount == 1:
                return value
