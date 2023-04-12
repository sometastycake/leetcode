# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = set()
        for value in sorted(nums):
            if value not in counter:
                counter.add(value)
            else:
                return True
        return False
