# https://leetcode.com/problems/most-frequent-even-element/

from collections import defaultdict
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for value in nums:
            if not value & 1:
                counter[value] += 1
        if not counter:
            return -1
        sortedCounter = list(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        i = 0
        result = sortedCounter[0][0]
        while i < len(sortedCounter) and sortedCounter[i][1] == sortedCounter[0][1]:
            if sortedCounter[i][0] < result:
                result = sortedCounter[i][0]
            i += 1
        return result
