# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
from typing import List


class Solution:

    def convert(self, s: str) -> int:
        result = 0
        for letter in s:
            if letter.isalpha():
                return len(s)
            result *= 10
            result += int(letter)
        return result

    def maximumValue(self, strs: List[str]) -> int:
        result = 0
        for s in strs:
            value = self.convert(s)
            if value > result:
                result = value
        return result
