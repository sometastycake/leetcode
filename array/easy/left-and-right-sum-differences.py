# https://leetcode.com/problems/left-and-right-sum-differences/

from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        rightSum = sum(nums)
        result = []
        leftSum = 0
        for i in range(len(nums)):
            rightSum -= nums[i]
            result.append(abs(leftSum - rightSum))
            leftSum += nums[i]
        return result
