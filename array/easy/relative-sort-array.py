# https://leetcode.com/problems/relative-sort-array/

from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        result = []
        for value in arr2:
            result += [value] * counter[value]
            del counter[value]
        for key in sorted(counter.keys()):
            result += [key] * counter[key]
        return result
