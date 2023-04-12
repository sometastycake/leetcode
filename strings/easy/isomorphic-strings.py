# https://leetcode.com/problems/isomorphic-strings/

from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mapping = {}
        counter = defaultdict(int)
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
                if counter[t[i]] > 0:
                    return False
                counter[t[i]] += 1
            else:
                if mapping[s[i]] != t[i] or counter[t[i]] > 1:
                    return False
        return True
