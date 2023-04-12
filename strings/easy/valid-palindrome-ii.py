# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        skipCount = 0
        prevI = prevJ = None
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if skipCount == 2:
                    return False
                if not skipCount:
                    prevI = i
                    prevJ = j
                    i += 1
                else:
                    i = prevI
                    j = prevJ
                    j -= 1
                skipCount += 1
        return True
