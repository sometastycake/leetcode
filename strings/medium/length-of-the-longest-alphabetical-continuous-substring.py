# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        result = 0
        prev = ''
        current = 0
        for letter in s:
            if not prev or chr(ord(letter) - 1) == prev:
                prev = letter
                current += 1
            else:
                if current > result:
                    result = current
                prev = letter
                current = 1
        if current > result:
            result = current
        return result
