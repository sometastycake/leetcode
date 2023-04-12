# https://leetcode.com/problems/word-subsets/

from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = defaultdict(int)
        for word in words2:
            subcounter = Counter(word)
            for letter, amount in subcounter.items():
                if letter not in counter:
                    counter[letter] = amount
                elif amount > counter[letter]:
                    counter[letter] = amount
        result = []
        for word in words1:
            currentCounter = Counter(word)
            for letter, amount in counter.items():
                if currentCounter[letter] < amount:
                    break
            else:
                result.append(word)
        return result
