# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:

    def reverse(self, num: int) -> int:
        result = 0
        k = 1
        while num:
            digit = num % 10
            result += digit * k
            k *= 10
            num //= 10
        return result

    def isSameAfterReversals(self, num: int) -> bool:
        if num < 10:
            return True
        if not num % 10:
            return False
        return self.reverse(self.reverse(num)) == num
