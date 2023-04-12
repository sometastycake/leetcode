# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

from collections import Counter
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums) // 2
        for value, amount in counter.items():
            if amount == n:
                return value
