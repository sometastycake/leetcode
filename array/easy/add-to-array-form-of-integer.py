# https://leetcode.com/problems/add-to-array-form-of-integer/

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = 0
        for digit in num:
            number *= 10
            number += digit
        result = number + k
        return [int(digit) for digit in str(result)]
