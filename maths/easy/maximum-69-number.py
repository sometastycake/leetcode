# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = list(str(num))
        for i, digit in enumerate(digits):
            if digit == '6':
                digits[i] = '9'
                return int(''.join(digits))
        return num
