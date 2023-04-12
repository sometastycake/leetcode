# https://leetcode.com/problems/fibonacci-number/

class Solution:

    def __init__(self):
        self.cache = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n in self.cache:
            return self.cache[n]
        result = self.fib(n - 1) + self.fib(n - 2)
        if n not in self.cache:
            self.cache[n] = result
        return result
