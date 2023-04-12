# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        cache = {}
        elementSum = 0
        digitSum = 0
        for value in nums:
            elementSum += value
            if value in cache:
                digitSum += cache[value]
                continue
            tmp = value
            currentDigitSum = 0
            while tmp:
                currentDigitSum += tmp % 10
                tmp //= 10
            cache[value] = currentDigitSum
            digitSum += currentDigitSum
        return abs(elementSum - digitSum)
