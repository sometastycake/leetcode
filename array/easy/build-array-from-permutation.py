# https://leetcode.com/problems/build-array-from-permutation/

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result
