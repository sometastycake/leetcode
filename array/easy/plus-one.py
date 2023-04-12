# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = 1
        for i in range(len(digits) - 1, -1, -1):
            result = digits[i] + m
            if result >= 10:
                digits[i] = result - 10
                m = 1
            else:
                m = 0
                digits[i] = result
                break
        if m:
            digits.insert(0, 1)
        return digits
