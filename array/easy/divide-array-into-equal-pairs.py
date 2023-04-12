# https://leetcode.com/problems/divide-array-into-equal-pairs/

from collections import defaultdict
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairs = defaultdict(int)
        for value in nums:
            pairs[value] += 1
        return all([not value % 2 for value in pairs.values()])
