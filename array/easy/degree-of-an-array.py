# https://leetcode.com/problems/degree-of-an-array/

from collections import defaultdict
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        indexes = {}
        for i, value in enumerate(nums):
            frequency[value] += 1
            if value not in indexes:
                indexes[value] = [i, i]
            else:
                indexes[value][1] = i
        sortedFrequency = list(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        maxFrequency = sortedFrequency[0][1]
        k = 0
        result = None
        while k < len(sortedFrequency) and sortedFrequency[k][1] == maxFrequency:
            value = sortedFrequency[k][0]
            i, j = indexes[value]
            if result is None:
                result = j - i + 1
            elif j - i + 1 < result:
                result = j - i + 1
            k += 1
        return result
