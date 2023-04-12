# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for letter in ransomNote:
            if letter not in counter:
                return False
            counter[letter] -= 1
            if counter[letter] < 0:
                return False
        return True
