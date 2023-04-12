# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        counter = defaultdict(int)
        for word in words:
            for letter in word:
                counter[letter] += 1
        k = len(words)
        for letter, amount in counter.items():
            if amount % k:
                return False
        return True
