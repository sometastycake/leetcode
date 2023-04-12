# https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if not n & 1:
            return n
        return n << 1
