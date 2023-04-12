# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            substr = s[i: i + 3]
            if len(substr) == 3 and len(set(substr)) == 3:
                result += 1
            i += 1
        return result
