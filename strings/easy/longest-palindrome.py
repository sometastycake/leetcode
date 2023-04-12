# https://leetcode.com/problems/longest-palindrome/

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        result = 0
        for letter, amount in counter.items():
            if not amount % 2:
                result += amount
            else:
                if not result % 2:
                    result += amount
                else:
                    result += (amount - 1)
        return result
