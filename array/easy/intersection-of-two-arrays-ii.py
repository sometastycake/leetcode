# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        values = defaultdict(int)
        if len(nums1) < len(nums2):
            primary = nums1
            secondary = nums2
        else:
            primary = nums2
            secondary = nums1
        for value in secondary:
            values[value] += 1
        result = []
        for value in primary:
            if values[value] > 0:
                result.append(value)
                values[value] -= 1
        return result
