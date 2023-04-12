# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for v in nums:
            if v >= 10 and v <= 99 or v >= 1000 and v <= 9999 or v >= 100000 and v <= 999999:
                result += 1
        return result
