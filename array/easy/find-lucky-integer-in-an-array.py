# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter()
        for value in arr:
            counter[value] += 1
        result = -1
        maxFreq = 0
        for value, freq in counter.items():
            if value == freq:
                if freq > maxFreq:
                    maxFreq = freq
                    result = value
        return result
