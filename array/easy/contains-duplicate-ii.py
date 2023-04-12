# https://leetcode.com/problems/contains-duplicate-ii/

from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = defaultdict(list)
        for i, value in enumerate(nums):
            counter[value].append(i)
            if len(counter[value]) >= 2:
                diff = abs(counter[value][0] - counter[value][-1])
                if diff > k:
                    del counter[value][0]
                else:
                    return True
        for value, indexes in counter.items():
            for i in range(len(indexes) - 1):
                for j in range(i + 1, len(indexes)):
                    diff = abs(indexes[i] - indexes[j])
                    if diff > k:
                        break
                    return True
        return False
