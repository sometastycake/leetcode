# https://leetcode.com/problems/count-the-digits-that-divide-a-number/submissions/910178183/

class Solution:
    def countDigits(self, num: int) -> int:
        result = 0
        number = num
        while num:
            digit = num % 10
            if digit and not number % digit:
                result += 1
            num //= 10
        return result
