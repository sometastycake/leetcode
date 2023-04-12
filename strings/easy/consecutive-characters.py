# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            currentLength = 1
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                currentLength += 1
                j += 1
            if currentLength > result:
                result = currentLength
            i = j
        return result
