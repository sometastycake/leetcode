# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = set()
        for i in range(len(nums)):
            j = i + 1
            if nums[i] in prev:
                continue
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            prev.add(nums[i])
