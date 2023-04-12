# https://leetcode.com/problems/maximum-ascending-subarray-sum/

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        i = 0
        while i < len(nums):
            value = nums[i]
            i += 1
            while i < len(nums) and nums[i - 1] < nums[i]:
                value += nums[i]
                i += 1
            if value > result:
                result = value
        return result
