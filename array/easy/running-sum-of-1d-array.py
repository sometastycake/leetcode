# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(nums[i] + result[-1])
        return result
