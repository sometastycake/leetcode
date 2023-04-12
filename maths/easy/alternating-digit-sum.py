# https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = []
        while n:
            digit = n % 10
            digits.append(digit)
            n //= 10
        sign = 1
        result = 0
        for digit in reversed(digits):
            result += digit * sign
            sign *= -1
        return result
