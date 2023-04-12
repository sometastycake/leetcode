# https://leetcode.com/problems/self-dividing-numbers/

from typing import List


class Solution:

    def checkNumber(self, number: int) -> bool:
        num = number
        while number:
            digit = number % 10
            if not digit or num % digit:
                return False
            number //= 10
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for n in range(left, right + 1):
            if self.checkNumber(n):
                result.append(n)
        return result
