# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, letter in enumerate(s):
            if counter[letter] == 1:
                return i
        return -1
