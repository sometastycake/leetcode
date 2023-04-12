# https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return True
        if num % 2:
            return False
        s = 0
        i = num // 2
        while 0 < i != s:
            if num % i:
                i -= 1
                continue
            s += i
            if not i % 2:
                i //= 2
            else:
                i -= 1
        return s == num
