# https://leetcode.com/problems/monotonic-array/

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) in (1, 2):
            return True
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
        if i == len(nums):
            return True
        if nums[i] < nums[i - 1]:
            def comparator(a, b) -> bool:
                return a <= b
        else:
            def comparator(a, b) -> bool:
                return a >= b
        while i < len(nums):
            if not comparator(nums[i], nums[i - 1]):
                return False
            i += 1
        return True
