# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged = []
        m = len(nums1)
        n = len(nums2)
        while i < m or j < n:
            if i >= m:
                merged.append(nums2[j])
                j += 1
            elif j >= n:
                merged.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        length = len(merged)
        is_even = not length % 2
        if is_even:
            return round((merged[length // 2] + merged[length // 2 - 1]) / 2, 4)
        return round(merged[length // 2], 4)
