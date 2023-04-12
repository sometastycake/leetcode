# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words:
            if word == s[i: i + len(word)]:
                i += len(word)
                if i == len(s):
                    return True
                continue
            return False
