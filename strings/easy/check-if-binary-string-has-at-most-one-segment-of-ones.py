# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 0
        segments = False
        while i < len(s):
            if s[i] == '0':
                i += 1
                continue
            if segments:
                return False
            while i < len(s) and s[i] == '1':
                i += 1
            segments = True
        return True
