# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        maxsize = 0
        substr = set()
        i, j = 0, 0
        while i < len(s):
            if s[i] in substr:
                substr.clear()
                substring = s[j:i]
                i = substring.index(s[i]) + j + 1
                j = i
            substr.add(s[i])
            if len(substr) > maxsize:
                maxsize = len(substr)
            i += 1
        return maxsize
