# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minValue = 9999
        maxValue = 0
        for value in nums:
            if value > maxValue:
                maxValue = value
            if value < minValue:
                minValue = value
        divisor = minValue
        while divisor:
            if not minValue % divisor and not maxValue % divisor:
                return divisor
            if divisor == minValue:
                divisor //= 2
            else:
                divisor -= 1
