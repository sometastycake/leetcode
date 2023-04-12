# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

from collections import Counter
from typing import List


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = Counter(s)
        for letter in t:
            if letter not in counter:
                return False
            counter[letter] -= 1
        return all(not value for value in counter.values())

    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words
        cache = set()
        i = 1
        while i < len(words):
            key = (words[i - 1], words[i])
            if key in cache:
                words.remove(words[i])
                continue
            if self.isAnagram(*key):
                words.remove(words[i])
                cache.add(key)
            else:
                i += 1
        return words
