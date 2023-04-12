# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'a'
        if n % 2:
            return 'a' * (n - 2) + 'bc'
        return 'a' * (n - 1) + 'b'
