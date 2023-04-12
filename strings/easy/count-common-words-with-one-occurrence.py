# https://leetcode.com/problems/count-common-words-with-one-occurrence/

from collections import defaultdict
from typing import List, Dict


class Solution:

    def count(self, words: List[str]) -> Dict[str, int]:
        counter = defaultdict(int)
        i = 0
        j = len(words) - 1
        while i <= j:
            counter[words[i]] += 1
            if i != j:
                counter[words[j]] += 1
            i += 1
            j -= 1
        return counter

    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1Counter = self.count(words1)
        words2Counter = self.count(words2)
        return len(set([word for word, amount in words1Counter.items() if amount == 1]).intersection(
            [word for word, amount in words2Counter.items() if amount == 1]
        ))
