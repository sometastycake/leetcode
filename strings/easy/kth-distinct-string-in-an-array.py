# https://leetcode.com/problems/kth-distinct-string-in-an-array/

from collections import defaultdict
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = defaultdict(int)
        indexes = {}
        for i, word in enumerate(arr):
            counter[word] += 1
            indexes[word] = i
        result = []
        for word, amount in counter.items():
            if amount == 1:
                result.append((word, indexes[word]))
        if len(result) < k or not result:
            return ''
        result = sorted(result, key=lambda item: item[1])
        return result[k - 1][0]
