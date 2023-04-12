# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t or not s:
            return True
        if len(t) < len(s):
            return False
        i = 0
        for letter in t:
            if i < len(s) and letter == s[i]:
                i += 1
            if i == len(s):
                return True
        return False
