# https://leetcode.com/problems/number-of-common-factors/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factor = a if a < b else b
        result = 0
        for i in range(factor, 0, -1):
            if not a % i and not b % i:
                result += 1
        return result
