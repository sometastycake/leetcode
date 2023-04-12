# https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return n
        commonSum = sum(range(1, n + 1))
        currentSum = 0
        middleValue = n // 2
        for i in range(n, 0, -1):
            if i == middleValue:
                return -1
            currentSum += i
            if currentSum == commonSum:
                return i
            commonSum -= i
        return -1
